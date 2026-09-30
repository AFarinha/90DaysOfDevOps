# Day 52 Validation

Executed on 2026-09-30 against kind Kubernetes v1.36.1. Concise output and selected excerpts replace screenshots under the repository working agreements.

## Inspect built-in namespaces and system Pods; eight existed before Metrics Server installation.

Exit code: 0

```text
NAME                 STATUS   AGE
default              Active   56d
kube-node-lease      Active   56d
kube-public          Active   56d
kube-system          Active   56d
local-path-storage   Active   56d
NAME                                                   READY   STATUS    RESTARTS       AGE
coredns-589f44dc88-92gdk                               1/1     Running   7 (38m ago)    56d
coredns-589f44dc88-gkgk7                               1/1     Running   7 (38m ago)    56d
etcd-devops-cluster-control-plane                      1/1     Running   10 (38m ago)   56d
kindnet-wmxjn                                          1/1     Running   7 (38m ago)    56d
kube-apiserver-devops-cluster-control-plane            1/1     Running   10 (38m ago)   56d
kube-controller-manager-devops-cluster-control-plane   1/1     Running   11 (38m ago)   56d
kube-proxy-vzp29                                       1/1     Running   7 (38m ago)    56d
kube-scheduler-devops-cluster-control-plane            1/1     Running   11 (38m ago)   56d
metrics-server-5b58578978-mwzdd                        1/1     Running   0              32s
```

## Create dev namespace.

Exit code: 0

```text
namespace/dev created
```

## Create staging namespace.

Exit code: 0

```text
namespace/staging created
```

## Validate namespace.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
namespace/production created (dry run)
```

## Validate namespace.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
namespace/production created (server dry run)
```

## Apply namespace.yaml.

Exit code: 0

```text
namespace/production created
```

## Create standalone Pod in dev namespace.

Exit code: 0

```text
pod/nginx-dev created
```

## Create standalone Pod in staging namespace.

Exit code: 0

```text
pod/nginx-staging created
```

## Validate nginx-deployment.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/nginx-deployment created (dry run)
```

## Validate nginx-deployment.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/nginx-deployment created (server dry run)
```

## Apply nginx-deployment.yaml.

Exit code: 0

```text
deployment.apps/nginx-deployment created
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for deployment "nginx-deployment" rollout to finish: 0 of 3 updated replicas are available...
Waiting for deployment "nginx-deployment" rollout to finish: 1 of 3 updated replicas are available...
Waiting for deployment "nginx-deployment" rollout to finish: 2 of 3 updated replicas are available...
deployment "nginx-deployment" successfully rolled out
```

## Compare default namespace output with all namespaces (-A).

Exit code: 0

```text
No resources found in default namespace.
NAMESPACE            NAME                                     READY   UP-TO-DATE   AVAILABLE   AGE
dev                  deployment.apps/nginx-deployment         3/3     3            3           59s
kube-system          deployment.apps/coredns                  2/2     2            2           56d
kube-system          deployment.apps/metrics-server           1/1     1            1           97s
local-path-storage   deployment.apps/local-path-provisioner   1/1     1            1           56d

NAMESPACE            NAME                                                       READY   STATUS    RESTARTS       AGE
dev                  pod/nginx-deployment-9ff74b9fb-4ncnr                       1/1     Running   0              59s
dev                  pod/nginx-deployment-9ff74b9fb-fmhgd                       1/1     Running   0              59s
dev                  pod/nginx-deployment-9ff74b9fb-zl278                       1/1     Running   0              59s
dev                  pod/nginx-dev                                              1/1     Running   0              62s
kube-system          pod/coredns-589f44dc88-92gdk                               1/1     Running   7 (39m ago)    56d
kube-system          pod/coredns-589f44dc88-gkgk7                               1/1     Running   7 (39m ago)    56d
kube-system          pod/etcd-devops-cluster-control-plane                      1/1     Running   10 (39m ago)   56d
kube-system          pod/kindnet-wmxjn                                          1/1     Running   7 (39m ago)    56d
kube-system          pod/kube-apiserver-devops-cluster-control-plane            1/1     Running   10 (39m ago)   56d
kube-system          pod/kube-controller-manager-devops-cluster-control-plane   1/1     Running   11 (39m ago)   56d
kube-system          pod/kube-proxy-vzp29                                       1/1     Running   7 (39m ago)    56d
kube-system          pod/kube-scheduler-devops-cluster-control-plane            1/1     Running   11 (39m ago)   56d
kube-system          pod/metrics-server-5b58578978-mwzdd                        1/1     Running   0              97s
local-path-storage   pod/local-path-provisioner-855c7b7774-zpbn5                1/1     Running   12 (38m ago)   56d
staging              pod/nginx-staging                                          1/1     Running   0              61s
```

## Choose managed Pod for replacement.

Exit code: 0

```text
nginx-deployment-9ff74b9fb-4ncnr
```

## Delete one managed Pod to test self-healing. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "nginx-deployment-9ff74b9fb-4ncnr" deleted from dev namespace
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
deployment "nginx-deployment" successfully rolled out
```

## Verify replacement has a new name.

Exit code: 0

```text
NAME                               READY   STATUS    RESTARTS   AGE
nginx-deployment-9ff74b9fb-fmhgd   1/1     Running   0          63s
nginx-deployment-9ff74b9fb-p8dsj   1/1     Running   0          3s
nginx-deployment-9ff74b9fb-zl278   1/1     Running   0          63s
nginx-dev                          1/1     Running   0          66s
```

## Scale desired replicas to 5.

Exit code: 0

```text
deployment.apps/nginx-deployment scaled
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for deployment "nginx-deployment" rollout to finish: 3 of 5 updated replicas are available...
Waiting for deployment "nginx-deployment" rollout to finish: 4 of 5 updated replicas are available...
deployment "nginx-deployment" successfully rolled out
```

## Inspect ready replica count.

Exit code: 0

```text
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx-deployment   5/5     5            5           66s

NAME                                   READY   STATUS    RESTARTS   AGE
pod/nginx-deployment-9ff74b9fb-fmhgd   1/1     Running   0          66s
pod/nginx-deployment-9ff74b9fb-gzxbk   1/1     Running   0          2s
pod/nginx-deployment-9ff74b9fb-jtdtt   1/1     Running   0          2s
pod/nginx-deployment-9ff74b9fb-p8dsj   1/1     Running   0          6s
pod/nginx-deployment-9ff74b9fb-zl278   1/1     Running   0          66s
pod/nginx-dev                          1/1     Running   0          69s
```

## Scale desired replicas to 2.

Exit code: 0

```text
deployment.apps/nginx-deployment scaled
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
deployment "nginx-deployment" successfully rolled out
```

## Inspect ready replica count.

Exit code: 0

```text
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx-deployment   2/2     2            2           68s

NAME                                   READY   STATUS    RESTARTS   AGE
pod/nginx-deployment-9ff74b9fb-fmhgd   1/1     Running   0          68s
pod/nginx-deployment-9ff74b9fb-zl278   1/1     Running   0          68s
pod/nginx-dev                          1/1     Running   0          71s
```

## Trigger rolling update to nginx:1.25.

Exit code: 0

```text
deployment.apps/nginx-deployment image updated
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "nginx-deployment" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "nginx-deployment" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "nginx-deployment" rollout to finish: 1 old replicas are pending termination...
deployment "nginx-deployment" successfully rolled out
```

## Inspect rollout revisions.

Exit code: 0

```text
deployment.apps/nginx-deployment
REVISION  CHANGE-CAUSE
1         <none>
2         <none>
```

## Roll back the Pod template.

Exit code: 0

```text
Warning: resource deployments/nginx-deployment was previously managed with 'kubectl apply'. Rolling back will not update the kubectl.kubernetes.io/last-applied-configuration annotation, which may cause unexpected behavior on future 'kubectl apply' operations. Consider using 'kubectl apply' with your previous configuration file instead.
deployment.apps/nginx-deployment rolled back
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "nginx-deployment" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "nginx-deployment" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "nginx-deployment" rollout to finish: 1 old replicas are pending termination...
deployment "nginx-deployment" successfully rolled out
```

## Verify rollback image.

Exit code: 0

```text
nginx:1.24
```

## Remove newly created namespaces and exercise resources. Deletes exercise resources; approval required.

Exit code: 0

```text
namespace "dev" deleted
namespace "staging" deleted
namespace "production" deleted
```

## Verify namespaces are gone.

Exit code: 0

```text
NAME                 STATUS   AGE
default              Active   56d
kube-node-lease      Active   56d
kube-public          Active   56d
kube-system          Active   56d
local-path-storage   Active   56d
```
