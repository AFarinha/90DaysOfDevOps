# Day 56 Validation

Executed on 2026-09-30 against kind Kubernetes v1.36.1. Concise output and selected excerpts replace screenshots under the repository working agreements.

## Validate comparison-deployment.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/comparison created (dry run)
```

## Validate comparison-deployment.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/comparison created (server dry run)
```

## Apply comparison-deployment.yaml.

Exit code: 0

```text
deployment.apps/comparison created
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
deployment "comparison" successfully rolled out
```

## Read random Deployment Pod name.

Exit code: 0

```text
comparison-69649c5ddd-fs555
```

## Test replacement with a different name. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "comparison-69649c5ddd-fs555" deleted from default namespace
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
deployment "comparison" successfully rolled out
```

## Inspect replacement names.

Exit code: 0

```text
NAME                          READY   STATUS    RESTARTS   AGE
comparison-69649c5ddd-8z4br   1/1     Running   0          9s
comparison-69649c5ddd-j8mws   1/1     Running   0          27s
comparison-69649c5ddd-v997g   1/1     Running   0          27s
```

## Remove comparison Deployment before StatefulSet. Deletes exercise resources; approval required.

Exit code: 0

```text
deployment.apps "comparison" deleted from default namespace
```

## Validate headless-service.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
service/web-headless created (dry run)
```

## Validate headless-service.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
service/web-headless created (server dry run)
```

## Apply headless-service.yaml.

Exit code: 0

```text
service/web-headless created
```

## Validate statefulset.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
statefulset.apps/web created (dry run)
```

## Validate statefulset.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
statefulset.apps/web created (server dry run)
```

## Apply statefulset.yaml.

Exit code: 0

```text
statefulset.apps/web created
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for 3 pods to be ready...
Waiting for 2 pods to be ready...
Waiting for 2 pods to be ready...
Waiting for 1 pods to be ready...
Waiting for 1 pods to be ready...
partitioned roll out complete: 3 new pods have been updated...
```

## Inspect ordered Pod names, per-replica PVCs and headless Service.

Exit code: 0

```text
NAME    READY   STATUS    RESTARTS   AGE   IP            NODE                           NOMINATED NODE   READINESS GATES
web-0   1/1     Running   0          25s   10.244.0.40   devops-cluster-control-plane   <none>           <none>
web-1   1/1     Running   0          19s   10.244.0.43   devops-cluster-control-plane   <none>           <none>
web-2   1/1     Running   0          11s   10.244.0.45   devops-cluster-control-plane   <none>           <none>
NAME             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
web-data-web-0   Bound    pvc-4c9e2a83-cc27-47e3-8543-f5615ca75ba1   100Mi      RWO            standard       <unset>                 27s
web-data-web-1   Bound    pvc-e856ee2d-7817-4289-8655-94a4a3bc3854   100Mi      RWO            standard       <unset>                 21s
web-data-web-2   Bound    pvc-82f14f47-06c0-4f39-8a9f-2d90b78061af   100Mi      RWO            standard       <unset>                 13s
NAME           TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
web-headless   ClusterIP   None         <none>        80/TCP    33s
```

## Resolve all three stable Pod DNS names; remove temporary client.

Exit code: 0

```text
Server:		10.96.0.10
Address:	10.96.0.10:53


Name:	web-0.web-headless.default.svc.cluster.local
Address: 10.244.0.40

Server:		10.96.0.10
Address:	10.96.0.10:53


Name:	web-1.web-headless.default.svc.cluster.local
Address: 10.244.0.43

Server:		10.96.0.10
Address:	10.96.0.10:53


Name:	web-2.web-headless.default.svc.cluster.local
Address: 10.244.0.45

All commands and output from this session will be recorded in container logs, including credentials and sensitive information passed through the command prompt.
If you don't see a command prompt, try pressing enter.
pod "stateful-dns" deleted from default namespace
```

## Write unique data to web-0 PVC.

Exit code: 0

```text

```

## Write unique data to web-1 PVC.

Exit code: 0

```text

```

## Write unique data to web-2 PVC.

Exit code: 0

```text

```

## Delete StatefulSet Pod while preserving identity and PVC. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "web-0" deleted from default namespace
```

## Wait for exercise Pods to become Ready (180-second timeout).

Exit code: 0

```text
pod/web-0 condition met
```

## Verify identical stored data after replacement.

Exit code: 0

```text
Data-from-web-0
```

## Scale StatefulSet to 5; creation uses ascending ordinals and removal descending.

Exit code: 0

```text
statefulset.apps/web scaled
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for 2 pods to be ready...
Waiting for 1 pods to be ready...
Waiting for 1 pods to be ready...
partitioned roll out complete: 5 new pods have been updated...
```

## Verify retained claims after scaling.

Exit code: 0

```text
NAME    READY   STATUS    RESTARTS   AGE
web-0   1/1     Running   0          18s
web-1   1/1     Running   0          51s
web-2   1/1     Running   0          43s
web-3   1/1     Running   0          14s
web-4   1/1     Running   0          7s
NAME             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
web-data-web-0   Bound    pvc-4c9e2a83-cc27-47e3-8543-f5615ca75ba1   100Mi      RWO            standard       <unset>                 58s
web-data-web-1   Bound    pvc-e856ee2d-7817-4289-8655-94a4a3bc3854   100Mi      RWO            standard       <unset>                 52s
web-data-web-2   Bound    pvc-82f14f47-06c0-4f39-8a9f-2d90b78061af   100Mi      RWO            standard       <unset>                 44s
web-data-web-3   Bound    pvc-9e62ab56-ba97-4666-bcc4-cb44e76161c8   100Mi      RWO            standard       <unset>                 15s
web-data-web-4   Bound    pvc-6aa18a7c-b48e-4825-8d36-d2768e66c883   100Mi      RWO            standard       <unset>                 8s
```

## Scale StatefulSet to 3; creation uses ascending ordinals and removal descending.

Exit code: 0

```text
statefulset.apps/web scaled
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
partitioned roll out complete: 4 new pods have been updated...
```

## Verify retained claims after scaling.

Exit code: 0

```text
NAME    READY   STATUS        RESTARTS   AGE
web-0   1/1     Running       0          21s
web-1   1/1     Running       0          54s
web-2   1/1     Running       0          46s
web-3   1/1     Terminating   0          17s
NAME             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
web-data-web-0   Bound    pvc-4c9e2a83-cc27-47e3-8543-f5615ca75ba1   100Mi      RWO            standard       <unset>                 61s
web-data-web-1   Bound    pvc-e856ee2d-7817-4289-8655-94a4a3bc3854   100Mi      RWO            standard       <unset>                 55s
web-data-web-2   Bound    pvc-82f14f47-06c0-4f39-8a9f-2d90b78061af   100Mi      RWO            standard       <unset>                 47s
web-data-web-3   Bound    pvc-9e62ab56-ba97-4666-bcc4-cb44e76161c8   100Mi      RWO            standard       <unset>                 18s
web-data-web-4   Bound    pvc-6aa18a7c-b48e-4825-8d36-d2768e66c883   100Mi      RWO            standard       <unset>                 11s
```

## Remove StatefulSet and headless Service. Deletes exercise resources; approval required.

Exit code: 0

```text
statefulset.apps "web" deleted from default namespace
service "web-headless" deleted from default namespace
```

## Verify five claims are retained after controller deletion.

Exit code: 0

```text
NAME             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
web-data-web-0   Bound    pvc-4c9e2a83-cc27-47e3-8543-f5615ca75ba1   100Mi      RWO            standard       <unset>                 66s
web-data-web-1   Bound    pvc-e856ee2d-7817-4289-8655-94a4a3bc3854   100Mi      RWO            standard       <unset>                 60s
web-data-web-2   Bound    pvc-82f14f47-06c0-4f39-8a9f-2d90b78061af   100Mi      RWO            standard       <unset>                 52s
web-data-web-3   Bound    pvc-9e62ab56-ba97-4666-bcc4-cb44e76161c8   100Mi      RWO            standard       <unset>                 23s
web-data-web-4   Bound    pvc-6aa18a7c-b48e-4825-8d36-d2768e66c883   100Mi      RWO            standard       <unset>                 16s
```

## Remove only StatefulSet exercise claims and dynamically provisioned data. Deletes exercise resources; approval required.

Exit code: 0

```text
persistentvolumeclaim "web-data-web-0" deleted from default namespace
persistentvolumeclaim "web-data-web-1" deleted from default namespace
persistentvolumeclaim "web-data-web-2" deleted from default namespace
persistentvolumeclaim "web-data-web-3" deleted from default namespace
persistentvolumeclaim "web-data-web-4" deleted from default namespace
```
