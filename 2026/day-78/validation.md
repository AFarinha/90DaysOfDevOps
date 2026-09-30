# Runtime Validation

Executed on 2026-09-30 in namespace `days71-80-lab`.

## SQL

```text

```
Exit code: 1

## Helm history

```text
REVISION	UPDATED                 	STATUS    	CHART       	APP VERSION	DESCRIPTION
1       	Wed Sep 30 15:49:34 2026	superseded	mysql-14.0.3	9.4.0      	Install complete
2       	Wed Sep 30 16:04:10 2026	superseded	mysql-14.0.3	9.4.0      	Upgrade complete
3       	Wed Sep 30 16:04:13 2026	deployed  	mysql-14.0.3	9.4.0      	Rollback to 1
4       	Wed Sep 30 16:20:22 2026	failed    	mysql-14.0.3	9.4.0      	Upgrade "bankapp-mysql" failed: resource StatefulSet/days71-80-lab/bankapp-mysql not ready. status: InProgress, message: Ready: ...
```

## SQL using the chart password-file environment

```text
Database
bankappdb
information_schema
mysql
performance_schema
sys
```
Exit code: 0
The first SQL attempt used the Docker image password variable; this Bitnami chart uses a password file instead.

## Final workloads before cleanup

```text
NAME                                                  READY   STATUS    RESTARTS   AGE
bankapp-mysql-0                                       2/2     Running   0          10m
bankapp-mysql-v2-0                                    2/2     Running   0          3m28s
lab-nginx-nginx-ingress-controller-8554498b4b-92b8z   1/1     Running   0          50m
my-bankapp-v2-bankapp-f54d78b4c-fdsjh                 1/1     Running   0          8m46s
my-bankapp-v2-bankapp-mysql-8f8dbbb8f-w9d86           1/1     Running   0          12m
my-bankapp-v2-bankapp-ollama-7846d74b45-8zpss         1/1     Running   0          8m42s
```

## Final release history

```text
REVISION	UPDATED                 	STATUS    	CHART       	APP VERSION	DESCRIPTION
1       	Wed Sep 30 15:49:34 2026	superseded	mysql-14.0.3	9.4.0      	Install complete
2       	Wed Sep 30 16:04:10 2026	superseded	mysql-14.0.3	9.4.0      	Upgrade complete
3       	Wed Sep 30 16:04:13 2026	superseded	mysql-14.0.3	9.4.0      	Rollback to 1
4       	Wed Sep 30 16:20:22 2026	failed    	mysql-14.0.3	9.4.0      	Upgrade "bankapp-mysql" failed: resource StatefulSet/days71-80-lab/bankapp-mysql not ready. status: InProgress, message: Ready: ...
5       	Wed Sep 30 16:36:58 2026	deployed  	mysql-14.0.3	9.4.0      	Upgrade complete
```

Recovered release revision 5 deployed successfully after the archived-image retry.
Second values-file release bankapp-mysql-v2 deployed successfully with Ready MySQL/exporter.
NGINX Ingress controller was Ready.

## Cleanup

All task-created lab containers, Compose networks/volumes and Helm releases were removed. The disposable namespace was deleted; the pre-existing devops-cluster was preserved. Dependencies, reference sources and package artifacts remain only in ignored local directories.
