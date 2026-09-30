# Day 60 - WordPress and MySQL Kubernetes Capstone

## Architecture

```text
HTTP client -> Node IP:30080 -> wordpress NodePort Service
                              -> WordPress Deployment (2 replicas, HPA 2-10)
                                 -> ConfigMap: database host/name
                                 -> Secret references: database user/password
                                 -> mysql-0.mysql.capstone.svc.cluster.local:3306
                                    -> mysql headless Service
                                    -> MySQL StatefulSet (1 replica)
                                       -> mysql-data-mysql-0 PVC (1Gi)
                                          -> standard local-path PV
```

All manual resources belong to capstone. [namespace.yaml](namespace.yaml) creates it. [mysql-service.yaml](mysql-service.yaml) supplies stable headless DNS. [mysql-statefulset.yaml](mysql-statefulset.yaml) runs mysql:8.0, imports the Secret with envFrom, mounts /var/lib/mysql, requests 250m CPU/512Mi and limits 500m CPU/1Gi. A TCP startup probe allows initialization before readiness is checked. The dynamically provisioned claim uses the verified standard StorageClass.

[create-secret.py](create-secret.py) renders stringData from environment variables and validates it with client and server dry-runs before applying through stdin. It stores no credentials on disk. Its four keys are MYSQL_ROOT_PASSWORD, MYSQL_DATABASE, MYSQL_USER and MYSQL_PASSWORD; the database and application user are both wordpress.

[wordpress-configmap.yaml](wordpress-configmap.yaml) defines the database DNS address and name. [wordpress-deployment.yaml](wordpress-deployment.yaml) runs wordpress:latest with two replicas, envFrom for public configuration and secretKeyRef for credentials. Each replica requests 250m CPU/128Mi and is limited to 500m CPU/256Mi. HTTP startup, liveness and readiness probes use /wp-login.php; five-second timeouts avoid the observed initialization failures. [wordpress-service.yaml](wordpress-service.yaml) exposes port 30080.

[wordpress-hpa.yaml](wordpress-hpa.yaml) targets CPU at 50%, minimum two and maximum ten, with explicit scale-up and scale-down behavior. It is applied after initialization and recovery testing, matching the task order. The kubeconfig default namespace was set to capstone during the exercise and restored to default during cleanup.

## Setup and actual recovery results

Both WordPress Pods and mysql-0 reached Ready. The MySQL application account listed the wordpress database. The setup wizard was reached at http://172.18.0.2:30080 and completed by [setup-wordpress.py](setup-wordpress.py), which submitted its HTTP form using a generated temporary admin password. No screenshot or credential was retained.

A published post was then created through WordPress's PHP application API. Its title was Day 60 persistence proof, with post ID 5.

| Check | Real result |
| --- | --- |
| Initial HTTP request | HTTP 200; published post visible through NodePort. |
| Delete one WordPress Pod | Deployment recreated it with a new name; the post remained visible. |
| Delete mysql-0 | StatefulSet recreated mysql-0 and reattached mysql-data-mysql-0. |
| HTTP after MySQL recovery | Original blog post remained visible. |
| Database after recovery | ID 5, original title, status publish. |
| HPA after samples arrived | CPU 3% (8m) against 50%; min 2, max 10, 2 current/desired replicas. |

## Failure and correction

The first one-second HTTP probe timeout was too short during installation, producing readiness failures and container restarts. Applying HPA before the installation wizard also reacted to startup CPU and created extra replicas. The correction added an HTTP startup probe, increased liveness/readiness timeouts to five seconds and raised the CPU request from 100m to 250m. The HPA was removed during setup and reapplied after the wizard and persistence checks. The corrected final stack had two ready WordPress Pods with zero restarts at the final snapshot.

This validates database-backed posts after Pod recreation. WordPress files and uploads are not shared or persisted in the manual Deployment. A post stored in MySQL survives, but a file uploaded only to one WordPress replica is outside this persistence guarantee.

## Bonus: Helm comparison

The first Bitnami WordPress installation exceeded its three-minute readiness timeout. It was cleaned up and repeated with chart version 34.1.1 and a five-minute budget, after images were cached. The retry succeeded: WordPress and MariaDB were both ready, and Helm reported deployed. The chart declared application version 7.1.2. Its default Service was LoadBalancer with a pending external IP on kind.

For a consistent comparison, deployment, statefulset, service, configmap, secret, pvc and hpa objects were counted by name. The manual namespace had nine and the Helm namespace twelve. Both counts include the automatic namespace root-CA ConfigMap; Helm's count also includes its release Secret. These are selected object counts, not a claim that kubectl get all lists every Kubernetes object.

The Helm chart supplies MariaDB rather than MySQL, an additional database Service, and persistent storage for WordPress itself. Helm reduces hand-written manifests and provides release-level upgrades; manual YAML exposes the exact choices directly. The bonus release and namespace, including retained claims, were removed after comparison.

## Concepts used

| Concept | Introduced | Capstone use |
| --- | --- | --- |
| Namespace | Day 52 | capstone and separate capstone-helm. |
| Deployment | Day 52 | WordPress replicas and recovery. |
| Service | Day 53 | NodePort HTTP and internal database access. |
| ConfigMap | Day 54 | Database host and name. |
| Secret | Day 54 | Database credentials through envFrom/secretKeyRef. |
| PV/PVC | Day 55 | Persistent MySQL data, dynamically provisioned. |
| StatefulSet | Day 56 | Stable mysql-0 identity. |
| Headless Service | Day 56 | Per-Pod database DNS. |
| Resource requests/limits | Day 57 | Scheduling, CPU and memory bounds. |
| Probes | Day 57 | Startup, readiness and liveness. |
| HPA | Day 58 | CPU target with two-to-ten replica bounds. |
| Helm | Day 59 | Separate packaged WordPress/MariaDB comparison. |

## Reflection and production gaps

The hardest part was distinguishing application initialization from steady-state health: overly short probes and premature autoscaling made startup unstable. Stable DNS plus per-replica storage made the database recovery behavior clear. A StatefulSet preserves identity and storage, but does not add database replication by itself.

For production, add shared/object storage for WordPress content, database backups and high availability, HTTPS ingress, meaningful health checks under traffic, external secret management, RBAC and NetworkPolicies, monitoring, and immutable image references. The current stack uses the README's latest WordPress tag and single-node local storage; it is a disposable learning environment.

## Validation and cleanup

Manifests passed client and server dry-runs; Python scripts passed syntax parsing without caches. Runtime tests, the failed initialization attempt, the successful corrections and both Helm attempts are recorded in [validation.md](validation.md). All exercise namespaces, claims and dynamically provisioned volumes were removed. The original default namespace was restored. Metrics Server remains installed as requested by Day 58. Repeatable commands, cleanup warnings and submission commands are in [tasks.md](tasks.md).
