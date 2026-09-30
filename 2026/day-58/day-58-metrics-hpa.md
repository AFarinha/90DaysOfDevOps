# Day 58 - Metrics Server and Horizontal Pod Autoscaler

## Resource metrics

Metrics Server aggregates recent kubelet CPU and memory usage for metrics.k8s.io, kubectl top and resource-based HPA decisions. It is not a historical monitoring database. The authorized install uses the official v0.9.0 manifest in [metrics-server.yaml](metrics-server.yaml). The only local-cluster adjustment is --kubelet-insecure-tls, because kind kubelet certificates are not verified here. Do not carry that exception into production.

The observed node snapshot was 1819m CPU (22%) and 869Mi memory (5%). The API server was the highest CPU Pod in that sample at 344m. Values vary with time and concurrent exercises. kubectl top shows actual usage, while describe shows configured requests and limits.

## Deployment and utilization

[php-apache-deployment.yaml](php-apache-deployment.yaml) uses registry.k8s.io/hpa-example with a 200m CPU request and 500m limit. [service.yaml](service.yaml) provides HTTP access. For CPU utilization, HPA compares usage against CPU requests; missing requests prevent that utilization calculation.

The imperative HPA targeted 50%, minimum one and maximum ten replicas. Its initial target was unknown until samples arrived. Under BusyBox HTTP load, it measured 190m, or 95% of the 200m request, and raised desired replicas from one to two. Evidence captured one ready Pod and the new second Pod being created; it does not claim ten replicas or a completed scale-down.

The basic calculation is desiredReplicas = ceil(currentReplicas * currentUtilization / targetUtilization). At one replica and 95%/50%, ceil(1.9) gives two. Controller tolerance, missing metrics, not-ready Pods, policies and stabilization can modify the actual decision.

## Declarative behavior

[hpa.yaml](hpa.yaml) uses autoscaling/v2, CPU at 50%, 1-10 replicas, immediate scale-up and a 300-second scale-down stabilization window. Its policies allow a 100% replica change per 15-second period; resource availability can still constrain the rollout. v1 supports CPU utilization, while v2 supports multiple resource, custom and external metrics with explicit behavior controls. The installed kubectl warns that --cpu-percent is deprecated; --cpu=50% is the current alternative.

## Validation and cleanup

Client and server dry-runs accepted the manifests. kubectl top returned data, the HPA emitted SuccessfulRescale to two, and v2 behavior was verified. Load, Service, Deployment and both HPA versions were removed. The five-minute scale-down window was not waited out, as allowed by the task. Metrics Server remains installed and Ready.

See [tasks.md](tasks.md), [validation.md](validation.md) and the [official Metrics Server project](https://github.com/kubernetes-sigs/metrics-server).
