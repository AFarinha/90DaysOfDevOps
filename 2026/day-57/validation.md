# Day 57 Validation

Executed on 2026-09-30 against kind Kubernetes v1.36.1. Concise output and selected excerpts replace screenshots under the repository working agreements.

## Validate resources-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/resources created (dry run)
```

## Validate resources-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/resources created (server dry run)
```

## Apply resources-pod.yaml.

Exit code: 0

```text
pod/resources created
```

## Validate oom-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/oom created (dry run)
```

## Validate oom-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/oom created (server dry run)
```

## Apply oom-pod.yaml.

Exit code: 0

```text
pod/oom created
```

## Validate pending-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/pending created (dry run)
```

## Validate pending-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/pending created (server dry run)
```

## Apply pending-pod.yaml.

Exit code: 0

```text
pod/pending created
```

## Validate liveness-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/liveness created (dry run)
```

## Validate liveness-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/liveness created (server dry run)
```

## Apply liveness-pod.yaml.

Exit code: 0

```text
pod/liveness created
```

## Validate readiness-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/readiness created (dry run)
```

## Validate readiness-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/readiness created (server dry run)
```

## Apply readiness-pod.yaml.

Exit code: 0

```text
pod/readiness created
```

## Validate startup-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/startup created (dry run)
```

## Validate startup-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/startup created (server dry run)
```

## Apply startup-pod.yaml.

Exit code: 0

```text
pod/startup created
```

## Wait for exercise Pods to become Ready (180-second timeout).

Exit code: 0

```text
pod/resources condition met
pod/readiness condition met
pod/startup condition met
```

## Inspect requests, limits and Burstable QoS.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
Status:           Running
    State:          Running
    Restart Count:  0
      cpu:     250m
      memory:  256Mi
      cpu:        100m
      memory:     128Mi
Conditions:
QoS Class:                   Burstable
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
```

## Wait for OOMKilled and verify exit 137.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
Status:           Running
      Reason:       CrashLoopBackOff
      Reason:       OOMKilled
      Exit Code:    137
    Restart Count:  1
      memory:  100Mi
      memory:     100Mi
Conditions:
QoS Class:                   Burstable
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
  Warning  BackOff    30s                kubelet            spec.containers{oom}: Back-off restarting failed container oom in pod oom_default(9a806630-bf93-4541-b0e9-17d974d31f8e)
```

## Inspect insufficient CPU and memory scheduling events.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
Status:           Pending
      cpu:        100
      memory:     128Gi
Conditions:
QoS Class:                   Burstable
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
  Warning  FailedScheduling  35s (x2 over 49s)  default-scheduler  0/1 nodes are available: 1 Insufficient cpu, 1 Insufficient memory. no new claims to deallocate, preemption: 0/1 nodes are available: 1 Preemption is not helpful for scheduling.
```

## Expose readiness Pod through Service.

Exit code: 0

```text
service/readiness-svc exposed
```

## Record ready endpoint before probe failure.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
      ready: true
      serving: true
```

## Remove disposable container index page to make readiness return HTTP 403.

Exit code: 0

```text

```

## Verify readiness false and endpoint ready=false without restart.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
NAME        READY   STATUS    RESTARTS   AGE
readiness   0/1     Running   0          49s
      ready: false
      serving: false
```

## Verify liveness restarts and startup success within the 60-second budget.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
Status:           Running
      touch /tmp/healthy; sleep 30; rm /tmp/healthy; sleep 3600
    State:          Running
      Reason:       Error
      Exit Code:    137
    Restart Count:  1
    Liveness:       exec [cat /tmp/healthy] delay=0s timeout=1s period=5s #success=1 #failure=3
Conditions:
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
  Warning  Unhealthy  11s (x3 over 21s)  kubelet            spec.containers{liveness}: Liveness probe failed: cat: can't open '/tmp/healthy': No such file or directory
  Normal   Killing    11s                kubelet            spec.containers{liveness}: Container liveness failed liveness probe, will be restarted
Name:             startup
Labels:           app=startup
Status:           Running
  startup:
    State:          Running
    Restart Count:  0
    Liveness:       exec [test -f /tmp/started] delay=0s timeout=1s period=5s #success=1 #failure=3
    Startup:        exec [test -f /tmp/started] delay=0s timeout=1s period=5s #success=1 #failure=12
Conditions:
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
  Normal   Scheduled  44s                default-scheduler  Successfully assigned default/startup to devops-cluster-control-plane
  Normal   Pulled     43s                kubelet            spec.containers{startup}: Container image "busybox:1.36" already present on machine and can be accessed by the pod
  Normal   Created    43s                kubelet            spec.containers{startup}: Container created
  Normal   Started    43s                kubelet            spec.containers{startup}: Container started
  Warning  Unhealthy  24s (x4 over 39s)  kubelet            spec.containers{startup}: Startup probe failed:
```

## Remove resource/probe Pods and Service. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "resources" deleted from default namespace
pod "oom" deleted from default namespace
pod "pending" deleted from default namespace
pod "liveness" deleted from default namespace
pod "readiness" deleted from default namespace
pod "startup" deleted from default namespace
service "readiness-svc" deleted from default namespace
```

## Verify exercises are cleaned up.

Exit code: 0

```text
NAME                                     READY   STATUS              RESTARTS   AGE
pod/my-nginx-67c767ddc4-ncxg6            1/1     Running             0          4m59s
pod/my-release-my-app-6b5f5cccf5-5mbdn   1/1     Running             0          4m14s
pod/my-release-my-app-6b5f5cccf5-662nw   1/1     Running             0          4m6s
pod/my-release-my-app-6b5f5cccf5-nzz58   1/1     Running             0          4m6s
pod/my-release-my-app-6b5f5cccf5-rkq9f   1/1     Running             0          4m14s
pod/my-release-my-app-6b5f5cccf5-sj65k   1/1     Running             0          4m14s
pod/my-release-my-app-test-connection    0/1     ContainerCreating   0          76s
pod/nginx-cli-849646c68b-drpgl           1/1     Running             0          2m21s
pod/nginx-cli-849646c68b-nvk4p           1/1     Running             0          2m21s
pod/nginx-cli-849646c68b-xwq4w           1/1     Running             0          2m21s
pod/nginx-values-6bd664fd74-564tw        1/1     Running             0          2m6s
pod/nginx-values-6bd664fd74-8pnqx        1/1     Running             0          2m6s
pod/nginx-values-6bd664fd74-dcjbl        1/1     Running             0          2m6s
pod/php-apache-7d4bd5f475-c2fsx          0/1     Terminating         0          2m21s
pod/php-apache-7d4bd5f475-snktx          1/1     Terminating         0          2m37s
pod/php-apache-7d4bd5f475-tjlt2          0/1     Terminating         0          2m36s
pod/php-apache-7d4bd5f475-vhjm7          1/1     Terminating         0          2m52s

NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
service/kubernetes          ClusterIP      10.96.0.1       <none>        443/TCP                      56d
service/my-nginx            LoadBalancer   10.96.212.3     <pending>     80:31646/TCP,443:30772/TCP   4m59s
service/my-release-my-app   ClusterIP      10.96.190.196   <none>        80/TCP                       4m14s
service/nginx-cli           NodePort       10.96.223.13    <none>        80:31899/TCP,443:31983/TCP   2m21s
service/nginx-values        NodePort       10.96.241.111   <none>        80:32339/TCP,443:31740/TCP   2m6s
```
