# Day 60 Validation

Executed on 2026-09-30 against kind Kubernetes v1.36.1. Concise output and selected excerpts replace screenshots under the repository working agreements.

## Validate namespace.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
namespace/capstone created (dry run)
```

## Validate namespace.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
namespace/capstone created (server dry run)
```

## Apply namespace.yaml.

Exit code: 0

```text
namespace/capstone created
```

## Generate disposable credentials in memory and apply Secret stringData through stdin.

Exit code: 0

```text
secret/mysql-secret created
```

## Validate mysql-service.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
service/mysql created (dry run)
```

## Validate mysql-service.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
service/mysql created (server dry run)
```

## Apply mysql-service.yaml.

Exit code: 0

```text
service/mysql created
```

## Validate mysql-statefulset.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
statefulset.apps/mysql created (dry run)
```

## Validate mysql-statefulset.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
statefulset.apps/mysql created (server dry run)
```

## Apply mysql-statefulset.yaml.

Exit code: 0

```text
statefulset.apps/mysql created
```

## Validate wordpress-configmap.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
configmap/wordpress-config created (dry run)
```

## Validate wordpress-configmap.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
configmap/wordpress-config created (server dry run)
```

## Apply wordpress-configmap.yaml.

Exit code: 0

```text
configmap/wordpress-config created
```

## Validate wordpress-deployment.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/wordpress created (dry run)
```

## Validate wordpress-deployment.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/wordpress created (server dry run)
```

## Apply wordpress-deployment.yaml.

Exit code: 0

```text
deployment.apps/wordpress created
```

## Validate wordpress-service.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
service/wordpress created (dry run)
```

## Validate wordpress-service.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
service/wordpress created (server dry run)
```

## Apply wordpress-service.yaml.

Exit code: 0

```text
service/wordpress created
```

## Validate wordpress-hpa.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling/wordpress created (dry run)
```

## Validate wordpress-hpa.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling/wordpress created (server dry run)
```

## Apply wordpress-hpa.yaml.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling/wordpress created
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for 1 pods to be ready...
partitioned roll out complete: 1 new pods have been updated...
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for deployment "wordpress" rollout to finish: 0 of 2 updated replicas are available...
Waiting for deployment "wordpress" rollout to finish: 1 of 2 updated replicas are available...
deployment "wordpress" successfully rolled out
```

## Verify wordpress database using existing container environment; do not print password.

Exit code: 0

```text
Database
information_schema
performance_schema
wordpress
```

## Inspect complete stack and MySQL claim before setup.

Exit code: 0

```text
NAME                             READY   STATUS    RESTARTS   AGE
pod/mysql-0                      1/1     Running   0          3m34s
pod/wordpress-5dc79c8b57-scn2z   1/1     Running   0          3m18s
pod/wordpress-5dc79c8b57-w7489   1/1     Running   0          3m17s

NAME                TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)        AGE
service/mysql       ClusterIP   None         <none>        3306/TCP       3m40s
service/wordpress   NodePort    10.96.5.21   <none>        80:30080/TCP   3m12s

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/wordpress   2/2     2            2           3m19s

NAME                                   DESIRED   CURRENT   READY   AGE
replicaset.apps/wordpress-5dc79c8b57   2         2         2       3m18s

NAME                     READY   AGE
statefulset.apps/mysql   1/1     3m35s

NAME                                            REFERENCE              TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
horizontalpodautoscaler.autoscaling/wordpress   Deployment/wordpress   cpu: <unknown>/50%   2         10        2          3m10s

NAME                                       STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
persistentvolumeclaim/mysql-data-mysql-0   Bound    pvc-47b0fb8f-628a-4183-b83a-63641b314f52   1Gi        RWO            standard       <unset>                 3m34s
```

## Set capstone as default after other namespace-dependent exercises finish.

Exit code: 0

```text
Context "kind-devops-cluster" modified.
```

## Complete HTTP installation wizard with a generated temporary admin password.

Exit code: 1

```text
[Selected excerpt; repetitive output and traceback internals omitted]
ConnectionRefusedError: [Errno 111] Connection refused
    with urllib.request.urlopen(base + "/wp-admin/install.php?step=1", timeout=30) as response:
urllib.error.URLError: <urlopen error [Errno 111] Connection refused>
```

## Pause autoscaling until the installation wizard finishes, following the task order. Deletes exercise resources; approval required.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling "wordpress" deleted from capstone namespace
```

## Validate wordpress-deployment.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/wordpress configured (dry run)
```

## Validate wordpress-deployment.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/wordpress configured (server dry run)
```

## Apply wordpress-deployment.yaml.

Exit code: 0

```text
deployment.apps/wordpress configured
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for deployment "wordpress" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "wordpress" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "wordpress" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "wordpress" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "wordpress" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "wordpress" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "wordpress" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "wordpress" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "wordpress" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "wordpress" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "wordpress" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "wordpress" rollout to finish: 1 old replicas are pending termination...
deployment "wordpress" successfully rolled out
```

## Complete HTTP installation wizard using a generated temporary admin password.

Exit code: 0

```text
WordPress HTTP installation wizard completed; credentials were not printed
```

## Publish the test blog post through the WordPress application API.

Exit code: 0

```text
Published test post ID: 5
```

## Verify published post over NodePort HTTP.

Exit code: 0

```text
HTTP 200: published persistence post visible
```

## Select a WordPress Pod for recovery testing.

Exit code: 0

```text
wordpress-b584c8f55-6r7ww
```

## Delete WordPress Pod to test Deployment recovery. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "wordpress-b584c8f55-6r7ww" deleted from capstone namespace
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
Waiting for deployment "wordpress" rollout to finish: 1 of 2 updated replicas are available...
deployment "wordpress" successfully rolled out
```

## Verify post after WordPress self-healing.

Exit code: 0

```text
Blog post visible after WordPress replacement
```

## Delete MySQL Pod while retaining its PVC. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "mysql-0" deleted from capstone namespace
```

## Wait for database Pod recovery.

Exit code: 0

```text
pod/mysql-0 condition met
```

## Verify blog post after database Pod recreation.

Exit code: 0

```text
Blog post visible after MySQL replacement: persistence verified
```

## Verify persisted post record without exposing credentials.

Exit code: 0

```text
ID	post_title	post_status
5	Day 60 persistence proof	publish
```

## Validate wordpress-hpa.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling/wordpress created (dry run)
```

## Validate wordpress-hpa.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling/wordpress created (server dry run)
```

## Apply wordpress-hpa.yaml.

Exit code: 0

```text
horizontalpodautoscaler.autoscaling/wordpress created
```

## Verify numeric CPU metrics, 50% target, minimum two and maximum ten.

Exit code: 0

```text
[Selected excerpt; repetitive output and traceback internals omitted]
NAME        REFERENCE              TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
wordpress   Deployment/wordpress   cpu: <unknown>/50%   2         10        0          1s
NAME        REFERENCE              TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
wordpress   Deployment/wordpress   cpu: <unknown>/50%   2         10        0          6s
NAME        REFERENCE              TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
wordpress   Deployment/wordpress   cpu: <unknown>/50%   2         10        0          12s
NAME        REFERENCE              TARGETS       MINPODS   MAXPODS   REPLICAS   AGE
wordpress   Deployment/wordpress   cpu: 3%/50%   2         10        2          19s
Name:                                                  wordpress
Reference:                                             Deployment/wordpress
Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  3% (8m) / 50%
Min replicas:                                          2
Max replicas:                                          10
  Scale Up:
    Stabilization Window: 0 seconds
    Select Policy: Max
  Scale Down:
    Stabilization Window: 300 seconds
    Select Policy: Max
Deployment pods:       2 current / 2 desired
  AbleToScale     True    ScaleDownStabilized  recent recommendations were higher than current one, applying the highest recent recommendation
  ScalingLimited  False   DesiredWithinRange   the desired count is within the acceptable range
```

## Record final running stack before authorized cleanup.

Exit code: 0

```text
NAME                            READY   STATUS    RESTARTS   AGE
pod/mysql-0                     1/1     Running   0          29s
pod/wordpress-b584c8f55-7ngmt   1/1     Running   0          95s
pod/wordpress-b584c8f55-clvml   1/1     Running   0          57s

NAME                TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)        AGE
service/mysql       ClusterIP   None         <none>        3306/TCP       12m
service/wordpress   NodePort    10.96.5.21   <none>        80:30080/TCP   12m

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/wordpress   2/2     2            2           12m

NAME                                   DESIRED   CURRENT   READY   AGE
replicaset.apps/wordpress-5dc79c8b57   0         0         0       12m
replicaset.apps/wordpress-b584c8f55    2         2         2       2m

NAME                     READY   AGE
statefulset.apps/mysql   1/1     12m

NAME                                            REFERENCE              TARGETS       MINPODS   MAXPODS   REPLICAS   AGE
horizontalpodautoscaler.autoscaling/wordpress   Deployment/wordpress   cpu: 3%/50%   2         10        2          21s

NAME                                       STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
persistentvolumeclaim/mysql-data-mysql-0   Bound    pvc-47b0fb8f-628a-4183-b83a-63641b314f52   1Gi        RWO            standard       <unset>                 12m
```

## Parse helper scripts without generating bytecode or installing dependencies.

Exit code: 0

```text
Python syntax valid
```

## Count manual stack objects using the selected comparison types (includes namespace bootstrap ConfigMap).

Exit code: 0

```text
9
```

## Verify revised Secret generator with existing credentials: client/server dry-runs, then idempotent apply; no values printed.

Exit code: 0

```text
secret/mysql-secret configured (dry run)
secret/mysql-secret configured (server dry run)
secret/mysql-secret configured
```

## Bonus: install Bitnami WordPress in a separate new namespace for comparison.

Exit code: 1

```text
Error: INSTALLATION FAILED: resource Deployment/capstone-helm/wp-helm-wordpress not ready. status: InProgress, message: Available: 0/1
context deadline exceeded
```

## Compare Helm-managed application resources with the manual stack.

Exit code: 0

```text
NAME                                    READY   STATUS    RESTARTS   AGE
pod/wp-helm-mariadb-0                   1/1     Running   0          3m
pod/wp-helm-wordpress-65cf4fc5b-h74qv   0/1     Running   0          3m

NAME                               TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)                      AGE
service/wp-helm-mariadb            ClusterIP      10.96.141.48   <none>        3306/TCP                     3m
service/wp-helm-mariadb-headless   ClusterIP      None           <none>        3306/TCP                     3m
service/wp-helm-wordpress          LoadBalancer   10.96.17.17    <pending>     80:32001/TCP,443:31398/TCP   3m

NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/wp-helm-wordpress   0/1     1            0           3m

NAME                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/wp-helm-wordpress-65cf4fc5b   1         1         0       3m

NAME                               READY   AGE
statefulset.apps/wp-helm-mariadb   1/1     3m

NAME                                           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
persistentvolumeclaim/data-wp-helm-mariadb-0   Bound    pvc-bab3f630-fab9-458a-9fd7-0b2855c5afb4   8Gi        RWO            standard       <unset>                 3m
persistentvolumeclaim/wp-helm-wordpress        Bound    pvc-598d9449-a953-427f-9ad1-02d3036e79c4   10Gi       RWO            standard       <unset>                 3m
NAME   	NAMESPACE    	REVISION	UPDATED                                	STATUS	CHART           	APP VERSION
wp-helm	capstone-helm	1       	2026-09-30 13:47:38.95296442 +0100 WEST	failed	wordpress-34.1.1	7.1.2
```

## Count selected named resource types in the Helm namespace; includes namespace bootstrap ConfigMap.

Exit code: 0

```text
12
```

## Uninstall bonus Helm release. Deletes exercise resources; approval required.

Exit code: 0

```text
release "wp-helm" uninstalled
```

## Remove bonus namespace and any retained claims/data. Deletes exercise resources; approval required.

Exit code: 0

```text
namespace "capstone-helm" deleted
```

## Delete completed manual capstone and its disposable database claim/data. Deletes exercise resources; approval required.

Exit code: 0

```text
namespace "capstone" deleted
```

## Restore original default namespace.

Exit code: 0

```text
Context "kind-devops-cluster" modified.
```

## Verify manual capstone cleanup and inspect remaining claims.

Exit code: 0

```text
NAME                 STATUS   AGE
default              Active   56d
kube-node-lease      Active   56d
kube-public          Active   56d
kube-system          Active   56d
local-path-storage   Active   56d
No resources found
```

## Retry bonus with pinned chart and five-minute initialization budget after the initial three-minute timeout.

Exit code: 0

```text
[Selected excerpt; repetitive output and traceback internals omitted]
NAME: wp-helm
NAMESPACE: capstone-helm
STATUS: deployed
REVISION: 1
TEST SUITE: None
CHART NAME: wordpress
** Please be patient while the chart is being deployed **
Your WordPress site can be accessed through the following DNS name from within your cluster:
    wp-helm-wordpress.capstone-helm.svc.cluster.local (port 80)
To access your WordPress site from outside the cluster follow the steps below:
1. Get the WordPress URL by running these commands:
  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        Watch the status with: 'kubectl get svc --namespace capstone-helm -w wp-helm-wordpress'
   export SERVICE_IP=$(kubectl get svc --namespace capstone-helm wp-helm-wordpress --template "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}")
   echo "WordPress URL: http://$SERVICE_IP/"
   echo "WordPress Admin URL: http://$SERVICE_IP/admin"
2. Open a browser and access WordPress using the obtained URL.
WARNING: no WordPress hostname provided and WordPress isn't exposed through Gateway API nor Ingress.
  Set the hostname via 'wordpressHost' or exposed WordPress via Gateway API / Ingress.
WARNING: Rolling tag detected (bitnami/wordpress:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
```

## Record bonus retry readiness and release state.

Exit code: 0

```text
NAME                                    READY   STATUS    RESTARTS   AGE
pod/wp-helm-mariadb-0                   1/1     Running   0          61s
pod/wp-helm-wordpress-65cf4fc5b-8gpp6   1/1     Running   0          62s

NAME                               TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
service/wp-helm-mariadb            ClusterIP      10.96.83.157    <none>        3306/TCP                     62s
service/wp-helm-mariadb-headless   ClusterIP      None            <none>        3306/TCP                     62s
service/wp-helm-wordpress          LoadBalancer   10.96.188.209   <pending>     80:32582/TCP,443:30597/TCP   62s

NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/wp-helm-wordpress   1/1     1            1           62s

NAME                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/wp-helm-wordpress-65cf4fc5b   1         1         1       62s

NAME                               READY   AGE
statefulset.apps/wp-helm-mariadb   1/1     62s

NAME                                           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
persistentvolumeclaim/data-wp-helm-mariadb-0   Bound    pvc-2ede2efd-7de0-4d69-a349-76d6d1b2896d   8Gi        RWO            standard       <unset>                 61s
persistentvolumeclaim/wp-helm-wordpress        Bound    pvc-b9480f06-f4ae-413a-95b1-d6a6a99d64a4   10Gi       RWO            standard       <unset>                 62s
NAME   	NAMESPACE    	REVISION	UPDATED                                 	STATUS  	CHART           	APP VERSION
wp-helm	capstone-helm	1       	2026-09-30 13:52:22.371144619 +0100 WEST	deployed	wordpress-34.1.1	7.1.2
```

## Count exactly the same selected resource types as the manual stack; includes Helm release Secret and namespace bootstrap ConfigMap.

Exit code: 0

```text
12
```

## Inspect initialization results without printing credentials.

Exit code: 0

```text
Defaulted container "wordpress" out of: wordpress, prepare-base-dir (init)
wordpress 12:53:04.75 INFO  ==> Installing WordPress
wordpress 12:53:13.76 INFO  ==> Persisting WordPress installation
Warning: option --restore=file is unsafe without option -P (--physical) as it traverses symbolic links in pathnames
Warning: option --restore=file is unsafe without option -P (--physical) as it traverses symbolic links in pathnames

wordpress 12:53:14.24 INFO  ==> ** WordPress setup finished! **
wordpress 12:53:14.25 INFO  ==> ** Starting Apache **
[Wed Sep 30 12:53:14.649974 2026] [ssl:notice] [pid 1:tid 1] AH01884: OpenSSL has FIPS mode enabled
[Wed Sep 30 12:53:14.712763 2026] [ssl:notice] [pid 1:tid 1] AH01884: OpenSSL has FIPS mode enabled
[Wed Sep 30 12:53:14.748548 2026] [mpm_prefork:notice] [pid 1:tid 1] AH00163: Apache/2.4.68 (Unix) OpenSSL/3.5.8 configured -- resuming normal operations
[Wed Sep 30 12:53:14.748611 2026] [core:notice] [pid 1:tid 1] AH00094: Command line: '/opt/bitnami/apache/bin/httpd -f /opt/bitnami/apache/conf/httpd.conf -D FOREGROUND'
10.244.0.1 - - [30/Sep/2026:12:53:22 +0000] "GET /wp-login.php HTTP/1.1" 200 5754
```

## Remove retried bonus release. Deletes exercise resources; approval required.

Exit code: 0

```text
release "wp-helm" uninstalled
```

## Remove retried namespace and retained storage. Deletes exercise resources; approval required.

Exit code: 0

```text
namespace "capstone-helm" deleted
```

## Verify final cleanup: no exercise namespaces, Pods, claims, volumes or Helm releases; Metrics Server is retained.

Exit code: 0

```text
NAME                 STATUS   AGE
default              Active   56d
kube-node-lease      Active   56d
kube-public          Active   56d
kube-system          Active   56d
local-path-storage   Active   56d
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   56d
No resources found
No resources found
NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
NAME             READY   UP-TO-DATE   AVAILABLE   AGE
metrics-server   1/1     1            1           31m
```

## Final repository checks

Passed: 39 YAML source files parsed, two Python scripts parsed without bytecode, 315 documented commands accepted by Bash syntax checking, all internal documentation links resolved, no trailing whitespace or credential payloads detected, and Helm lint passed. All 88 new files are inside days 52-60. No README was edited. No screenshots, caches, archives or tool binaries were added.
