# Day 58 Validation

Executed on 2026-09-30 against kind Kubernetes v1.36.1. Concise output and selected excerpts replace screenshots under the repository working agreements.

## Download pinned official Metrics Server v0.9.0 manifests.

Exit code: 0

```text

```

## Validate metrics-server.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
serviceaccount/metrics-server created (dry run)
clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader created (dry run)
clusterrole.rbac.authorization.k8s.io/system:metrics-server created (dry run)
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader created (dry run)
clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator created (dry run)
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server created (dry run)
service/metrics-server created (dry run)
deployment.apps/metrics-server created (dry run)
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io created (dry run)
```

## Validate metrics-server.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
serviceaccount/metrics-server created (server dry run)
clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader created (server dry run)
clusterrole.rbac.authorization.k8s.io/system:metrics-server created (server dry run)
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader created (server dry run)
clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator created (server dry run)
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server created (server dry run)
service/metrics-server created (server dry run)
deployment.apps/metrics-server created (server dry run)
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io created (server dry run)
```

## Apply metrics-server.yaml.

Exit code: 0

```text
serviceaccount/metrics-server created
clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader created
clusterrole.rbac.authorization.k8s.io/system:metrics-server created
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader created
clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator created
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server created
service/metrics-server created
deployment.apps/metrics-server created
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io created
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for deployment "metrics-server" rollout to finish: 0 of 1 updated replicas are available...
deployment "metrics-server" successfully rolled out
```

## Verify metrics API and inspect actual CPU/memory usage sorted by CPU.

Exit code: 0

```text
NAME                           CPU(cores)   CPU(%)   MEMORY(bytes)   MEMORY(%)
devops-cluster-control-plane   1819m        22%      869Mi           5%
NAMESPACE            NAME                                                   CPU(cores)   MEMORY(bytes)
kube-system          kube-apiserver-devops-cluster-control-plane            344m         232Mi
kube-system          etcd-devops-cluster-control-plane                      200m         99Mi
kube-system          kube-controller-manager-devops-cluster-control-plane   99m          54Mi
kube-system          kube-scheduler-devops-cluster-control-plane            66m          23Mi
kube-system          metrics-server-5b58578978-mwzdd                        20m          19Mi
kube-system          coredns-589f44dc88-92gdk                               9m           13Mi
kube-system          coredns-589f44dc88-gkgk7                               9m           13Mi
kube-system          kindnet-wmxjn                                          8m           22Mi
kube-system          kube-proxy-vzp29                                       8m           18Mi
local-path-storage   local-path-provisioner-855c7b7774-zpbn5                1m           9Mi
```

## Validate php-apache-deployment.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/php-apache created (dry run)
```

## Validate php-apache-deployment.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/php-apache created (server dry run)
```

## Apply php-apache-deployment.yaml.

Exit code: 0

```text
deployment.apps/php-apache created
```

## Validate service.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
service/php-apache created (dry run)
```

## Validate service.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
service/php-apache created (server dry run)
```

## Apply service.yaml.

Exit code: 0

```text
service/php-apache created
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for deployment "php-apache" rollout to finish: 0 of 1 updated replicas are available...
deployment "php-apache" successfully rolled out
```

## Read initial PHP server usage.

Exit code: 1

```text
error: metrics not available yet
```

## Create imperative CPU HPA; target 50% of 200m requests, bounded 1-10 replicas.

Exit code: 0

```text
Flag --cpu-percent has been deprecated, Use --cpu with percentage or resource quantity format (e.g., '70%' for utilization or '500m' for milliCPU).
horizontalpodautoscaler.autoscaling/php-apache autoscaled
```

## Inspect initial target and HPA conditions.

Exit code: 0

```text
NAME         REFERENCE               TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   cpu: <unknown>/50%   1         10        0          1s
Name:                                                  php-apache
Namespace:                                             default
Labels:                                                <none>
Annotations:                                           <none>
CreationTimestamp:                                     Wed, 30 Sep 2026 13:35:34 +0100
Reference:                                             Deployment/php-apache
Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  <unknown> / 50%
Min replicas:                                          1
Max replicas:                                          10
Deployment pods:                                       0 current / 0 desired
Events:                                                <none>
```

## Generate continuous HTTP load without storing response bodies.

Exit code: 0

```text
pod/load-generator created
```

## Observe autoscaling for up to 180 seconds and require increased replicas.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
NAME         REFERENCE               TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   cpu: <unknown>/50%   1         10        1          16s
NAME         REFERENCE               TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   cpu: <unknown>/50%   1         10        1          24s
NAME         REFERENCE               TARGETS        MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   cpu: 95%/50%   1         10        1          32s
NAME                              READY   STATUS              RESTARTS   AGE
pod/php-apache-7d4bd5f475-srp66   1/1     Running             0          117s
Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  95% (190m) / 50%
Min replicas:                                          1
Max replicas:                                          10
Deployment pods:                                       1 current / 2 desired
Conditions:
  AbleToScale     True    SucceededRescale    the HPA controller was able to update the target scale to 2
  ScalingActive   True    ValidMetricFound    the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)
  ScalingLimited  False   DesiredWithinRange  the desired count is within the acceptable range
  Warning  FailedGetResourceMetric       20s   horizontal-pod-autoscaler  failed to get cpu utilization: unable to get metrics for resource cpu: no metrics returned from resource metrics API
  Warning  FailedComputeMetricsReplicas  20s   horizontal-pod-autoscaler  invalid metrics (1 invalid out of 1), first error is: failed to get cpu resource metric value: failed to get cpu utilization: unable to get metrics for resource cpu: no metrics returned from resource metrics API
  Normal   SuccessfulRescale             5s    horizontal-pod-autoscaler  New size: 2; reason: cpu resource utilization (percentage of request) above target
```

## Stop load generator. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "load-generator" deleted from default namespace
```

## Remove imperative HPA before declarative replacement. Deletes exercise resources; approval required.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling "php-apache" deleted from default namespace
```

## Validate hpa.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling/php-apache created (dry run)
```

## Validate hpa.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling/php-apache created (server dry run)
```

## Apply hpa.yaml.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling/php-apache created
```

## Verify autoscaling/v2 policies: immediate scale-up, 300-second scale-down stabilization.

Exit code: 0

```text
Name:                                                  php-apache
Namespace:                                             default
Labels:                                                <none>
Annotations:                                           <none>
CreationTimestamp:                                     Wed, 30 Sep 2026 13:36:43 +0100
Reference:                                             Deployment/php-apache
Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  <unknown> / 50%
Min replicas:                                          1
Max replicas:                                          10
Behavior:
  Scale Up:
    Stabilization Window: 0 seconds
    Select Policy: Max
    Policies:
      - Type: Percent  Value: 100  Period: 15 seconds
  Scale Down:
    Stabilization Window: 300 seconds
    Select Policy: Max
    Policies:
      - Type: Percent  Value: 100  Period: 15 seconds
Deployment pods:       0 current / 0 desired
Events:                <none>
```

## Remove workload and HPA; leave authorized Metrics Server installed. Deletes exercise resources; approval required.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling "php-apache" deleted from default namespace
service "php-apache" deleted from default namespace
deployment.apps "php-apache" deleted from default namespace
```

## Verify Metrics Server remains operational after cleanup.

Exit code: 0

```text
NAME             READY   UP-TO-DATE   AVAILABLE   AGE
metrics-server   1/1     1            1           9m46s
NAME                           CPU(cores)   CPU(%)   MEMORY(bytes)   MEMORY(%)
devops-cluster-control-plane   1071m        13%      1203Mi          7%
```
