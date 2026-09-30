# Day 57 - Resource Requests, Limits and Probes

## Scheduling and enforcement

Requests express expected resource demand used for scheduling. Limits bound runtime usage. CPU over a limit is throttled; exceeding a memory limit can cause an OOM kill. A request is not a dedicated CPU core or a fixed reservation of physical memory. 100m means 0.1 CPU; Mi and Gi are binary memory units.

[resources-pod.yaml](resources-pod.yaml) requests 100m/128Mi and limits 250m/256Mi; observed QoS was Burstable. Guaranteed requires CPU and memory requests and limits on every container with equal values. BestEffort has none; other configurations are Burstable.

[oom-pod.yaml](oom-pod.yaml) allocates 200M under a 100Mi limit with polinux/stress. Its terminated state reported OOMKilled and exit code 137. Exit 137 alone means SIGKILL and does not prove OOM: the liveness example also exited 137 with Reason Error. Inspect the termination reason and events.

[pending-pod.yaml](pending-pod.yaml) requests 100 CPUs and 128Gi. The real scheduler reported 1 Insufficient cpu, 1 Insufficient memory and that preemption was not helpful.

## Three different health checks

| Probe | Manifest | Observed effect |
| --- | --- | --- |
| Liveness | [liveness-pod.yaml](liveness-pod.yaml) | Removing /tmp/healthy after 30 seconds caused three probe failures and a restart; restart count was one at verification. |
| Readiness | [readiness-pod.yaml](readiness-pod.yaml) | Removing the Nginx index caused HTTP 403 and 0/1 readiness; restart count stayed zero. |
| Startup | [startup-pod.yaml](startup-pod.yaml) | A 20-second initialization succeeded within a nominal 12 x 5 = 60 second budget; zero restarts. |

Readiness failure disables normal Service routing. EndpointSlice retained the address but changed ready and serving from true to false; it did not literally remove all addresses. Liveness failure restarts the container. Startup gates liveness and readiness until initialization succeeds; repeated startup failures restart the container. Reducing startup failureThreshold to two would give roughly ten seconds and likely restart this 20-second initialization before it completes. That reduced-threshold case was reasoned about, not executed.

The liveness Pod uses a one-second termination grace period to keep the experiment bounded. Probe timing is approximate and includes scheduling and execution delays.

## Validation and cleanup

All six Pod manifests passed client and server dry-runs. OOM, Pending, readiness, liveness and startup observations came from the real cluster. Exercise Pods and readiness-svc were removed. Commands and evidence are in [tasks.md](tasks.md) and [validation.md](validation.md).
