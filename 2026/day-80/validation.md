
## Helm history

```text
REVISION    UPDATED                     STATUS      CHART           APP VERSION DESCRIPTION
1           Wed Sep 30 16:01:48 2026    failed      bankapp-0.1.0   1.0.0       Release "my-bankapp-v2" failed: resource Deployment/days71-80-lab/my-bankapp-v2-bankapp not ready. status: InProgress, message: Available: 0/1
                                                                                resource Deployment/days71-80-lab/my-bankapp-v2-bankapp-ollama not ready. status: InProgress, message: Available: 0/1
                                                                                context deadline exceeded
2           Wed Sep 30 16:18:11 2026    failed      bankapp-0.2.0   1.1.0       Upgrade "my-bankapp-v2" failed: server-side apply failed for object days71-80-lab/my-bankapp-v2-bankapp-mysql-pvc /v1, Kind=PersistentVolumeClaim: PersistentVolumeClaim "my-bankapp-v2-bankapp-mysql-pvc" is invalid: spec.resources.requests.storage: Forbidden: field can not be less than status.capacity
3           Wed Sep 30 16:20:04 2026    failed      bankapp-0.2.0   1.1.0       Upgrade "my-bankapp-v2" failed: resource Deployment/days71-80-lab/my-bankapp-v2-bankapp not ready. status: InProgress, message: Pending termination: 1
                                                                                resource Deployment/days71-80-lab/my-bankapp-v2-bankapp-mysql not ready. status: InProgress, message: Available: 0/1
                                                                                context deadline exceeded
4           Wed Sep 30 16:27:43 2026    superseded  bankapp-0.2.0   1.1.0       Upgrade "my-bankapp-v2" failed: resource Deployment/days71-80-lab/my-bankapp-v2-bankapp not ready. status: Failed, message: Progress deadline exceeded
5           Wed Sep 30 16:31:26 2026    deployed    bankapp-0.2.0   1.1.0       Upgrade complete
```

## Final workloads before cleanup

```text
NAME                                                  READY   STATUS    RESTARTS   AGE
bankapp-mysql-0                                       2/2     Running   0          10m
bankapp-mysql-v2-0                                    2/2     Running   0          3m29s
lab-nginx-nginx-ingress-controller-8554498b4b-92b8z   1/1     Running   0          50m
my-bankapp-v2-bankapp-f54d78b4c-fdsjh                 1/1     Running   0          8m47s
my-bankapp-v2-bankapp-mysql-8f8dbbb8f-w9d86           1/1     Running   0          12m
my-bankapp-v2-bankapp-ollama-7846d74b45-8zpss         1/1     Running   0          8m43s
```

## Final release history

```text
REVISION    UPDATED                     STATUS      CHART           APP VERSION DESCRIPTION
1           Wed Sep 30 16:01:48 2026    failed      bankapp-0.1.0   1.0.0       Release "my-bankapp-v2" failed: resource Deployment/days71-80-lab/my-bankapp-v2-bankapp not ready. status: InProgress, message: Available: 0/1
                                                                                resource Deployment/days71-80-lab/my-bankapp-v2-bankapp-ollama not ready. status: InProgress, message: Available: 0/1
                                                                                context deadline exceeded
2           Wed Sep 30 16:18:11 2026    failed      bankapp-0.2.0   1.1.0       Upgrade "my-bankapp-v2" failed: server-side apply failed for object days71-80-lab/my-bankapp-v2-bankapp-mysql-pvc /v1, Kind=PersistentVolumeClaim: PersistentVolumeClaim "my-bankapp-v2-bankapp-mysql-pvc" is invalid: spec.resources.requests.storage: Forbidden: field can not be less than status.capacity
3           Wed Sep 30 16:20:04 2026    failed      bankapp-0.2.0   1.1.0       Upgrade "my-bankapp-v2" failed: resource Deployment/days71-80-lab/my-bankapp-v2-bankapp not ready. status: InProgress, message: Pending termination: 1
                                                                                resource Deployment/days71-80-lab/my-bankapp-v2-bankapp-mysql not ready. status: InProgress, message: Available: 0/1
                                                                                context deadline exceeded
4           Wed Sep 30 16:27:43 2026    superseded  bankapp-0.2.0   1.1.0       Upgrade "my-bankapp-v2" failed: resource Deployment/days71-80-lab/my-bankapp-v2-bankapp not ready. status: Failed, message: Progress deadline exceeded
5           Wed Sep 30 16:31:26 2026    deployed    bankapp-0.2.0   1.1.0       Upgrade complete
```

Full stack revision 5 deployed successfully; database readiness hook completed.
`helm test my-bankapp-v2 -n days71-80-lab --timeout 120s`: Phase Succeeded.
HTTP `/actuator/health`: 200, status UP; HTTP `/login`: 200, title Login - BankApp.
Ollama contained tinyllama:latest, 637 MB.
Lint and render passed for dev/staging/prod. Archives 0.1.0 and 0.2.0 were generated locally and excluded from Git.

## Cleanup

All task-created lab containers, Compose networks/volumes and Helm releases were removed. The disposable namespace was deleted; the pre-existing devops-cluster was preserved. Dependencies, reference sources and package artifacts remain only in ignored local directories.
