# Runtime Validation

Executed on 2026-09-30 in namespace `days71-80-lab`.

## SQL

```text
Database
bankappdb
information_schema
mysql
performance_schema
sys

```
Exit code: 0

## Ollama model

```text
NAME                ID              SIZE      MODIFIED
tinyllama:latest    2644915ede35    637 MB    2 minutes ago
```

HTTP /actuator/health: 200; {"status":"UP","groups":["liveness","readiness"]}

HTTP /login: 200; title=['Login - BankApp']; login form=True

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

## Cleanup

All task-created lab containers, Compose networks/volumes and Helm releases were removed. The disposable namespace was deleted; the pre-existing devops-cluster was preserved. Dependencies, reference sources and package artifacts remain only in ignored local directories.
