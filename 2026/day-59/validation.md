# Day 59 Validation

Executed on 2026-09-30 against kind Kubernetes v1.36.1. Concise output and selected excerpts replace screenshots under the repository working agreements.

## Download official Helm v4.3.0 archive into temporary storage.

Exit code: 0

```text

```

## Download the official archive checksum.

Exit code: 0

```text

```

## Verify Helm archive integrity.

Exit code: 1

```text
sha256sum: helm-v4.3.0-linux-amd64.tar.gz: No such file or directory
helm-v4.3.0-linux-amd64.tar.gz: FAILED open or read
sha256sum: WARNING: 1 listed file could not be read
```

## Verify SHA256 against the downloaded official checksum.

Exit code: 0

```text
Helm checksum verified
```

## Extract and install Helm in ~/.local/bin without sudo.

Exit code: 0

```text

```

## Verify installed Helm version.

Exit code: 127

```text
/bin/bash: line 1: helm: command not found
```

## Make user-local tools available in Bash and verify Helm version.

Exit code: 0

```text
v4.3.0+gbec5b06
```

## Inspect Helm configuration paths.

Exit code: 0

```text
HELM_BIN="helm"
HELM_BURST_LIMIT="100"
HELM_CACHE_HOME="/home/afarinha/.cache/helm"
HELM_CONFIG_HOME="/home/afarinha/.config/helm"
HELM_CONTENT_CACHE="/home/afarinha/.cache/helm/content"
HELM_DATA_HOME="/home/afarinha/.local/share/helm"
HELM_DEBUG="false"
HELM_KUBEAPISERVER=""
HELM_KUBEASGROUPS=""
HELM_KUBEASUSER=""
HELM_KUBECAFILE=""
HELM_KUBECONTEXT=""
HELM_KUBEINSECURE_SKIP_TLS_VERIFY="false"
HELM_KUBETLS_SERVER_NAME=""
HELM_KUBETOKEN=""
HELM_MAX_HISTORY="10"
HELM_NAMESPACE="default"
HELM_PLUGINS="/home/afarinha/.local/share/helm/plugins"
HELM_QPS="0.00"
HELM_REGISTRY_CONFIG="/home/afarinha/.config/helm/registry/config.json"
HELM_REPOSITORY_CACHE="/home/afarinha/.cache/helm/repository"
HELM_REPOSITORY_CONFIG="/home/afarinha/.config/helm/repositories.yaml"
```

## Add Bitnami chart repository.

Exit code: 0

```text
"bitnami" has been added to your repositories
```

## Refresh chart repository index.

Exit code: 0

```text
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "bitnami" chart repository
Update Complete. ?Happy Helming!?
```

## Search available Nginx charts.

Exit code: 0

```text
NAME                            	CHART VERSION	APP VERSION	DESCRIPTION
bitnami/nginx                   	25.2.1       	1.31.6     	NGINX Open Source is a web server that can be a...
bitnami/nginx-ingress-controller	12.0.7       	1.13.1     	NGINX Ingress Controller is an Ingress controll...
bitnami/nginx-intel             	2.1.15       	0.4.9      	DEPRECATED NGINX Open Source for Intel is a lig...
```

## Count Bitnami charts without listing full index.

Exit code: 0

```text
Bitnami chart count: 144
```

## Verify chart version and application version.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
annotations:
  fips: "true"
  images: |
    - name: git
      version: 2.56.0
      image: registry-1.docker.io/bitnami/git:latest
    - name: nginx
      version: 1.31.6
      image: registry-1.docker.io/bitnami/nginx:latest
    - name: nginx-exporter
      version: 1.5.3
      image: registry-1.docker.io/bitnami/nginx-exporter:latest
- reverse proxy
maintainers:
- name: Broadcom, Inc. All Rights Reserved.
  url: https://github.com/bitnami/charts
name: nginx
sources:
- https://github.com/bitnami/charts/tree/main/bitnami/nginx
version: 25.2.1
```

## Inspect defaults via a temporary file; avoid duplicating the full chart values.

Exit code: 0

```text

```

## Scaffold the custom application chart.

Exit code: 0

```text
Creating my-app
```

## Validate chart structure and templates.

Exit code: 0

```text
==> Linting my-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

## Render custom chart without installation.

Exit code: 0

```text

```

## Validate rendered manifests locally and on API server.

Exit code: 0

```text
serviceaccount/my-release-my-app created (dry run)
service/my-release-my-app created (dry run)
deployment.apps/my-release-my-app created (dry run)
pod/my-release-my-app-test-connection created (dry run)
serviceaccount/my-release-my-app created (server dry run)
service/my-release-my-app created (server dry run)
deployment.apps/my-release-my-app created (server dry run)
pod/my-release-my-app-test-connection created (server dry run)
```

## Install pinned Bitnami Nginx chart.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
NAME: my-nginx
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
CHART NAME: nginx
? WARNING: Since August 28th, 2025, only a limited subset of images/charts are available for free.
** Please be patient while the chart is being deployed **
  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
WARNING: Rolling tag detected (bitnami/nginx:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: Rolling tag detected (bitnami/git:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: Rolling tag detected (bitnami/nginx-exporter:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
```

## Inspect chart resources and release status.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
NAME                            READY   STATUS     RESTARTS   AGE
NAME               TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)                      AGE
service/my-nginx   LoadBalancer   10.96.212.3   <pending>     80:31646/TCP,443:30772/TCP   2s
NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
NAME                                  DESIRED   CURRENT   READY   AGE
NAME    	NAMESPACE	REVISION	UPDATED                                 	STATUS  	CHART       	APP VERSION
my-nginx	default  	1       	2026-09-30 13:33:53.187327374 +0100 WEST	deployed	nginx-25.2.1	1.31.6
NAME: my-nginx
NAMESPACE: default
STATUS: deployed
REVISION: 1
NAME       TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)                      AGE
my-nginx   LoadBalancer   10.96.212.3   <pending>     80:31646/TCP,443:30772/TCP   7s
NAME       READY   UP-TO-DATE   AVAILABLE   AGE
NAME                        READY   STATUS     RESTARTS   AGE
==> v1/NetworkPolicy
NAME       POD-SELECTOR                                                       AGE
NAME       MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
NAME       AGE
NAME           TYPE                DATA   AGE
TEST SUITE: None
CHART NAME: nginx
? WARNING: Since August 28th, 2025, only a limited subset of images/charts are available for free.
** Please be patient while the chart is being deployed **
  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
WARNING: Rolling tag detected (bitnami/nginx:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: Rolling tag detected (bitnami/git:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: Rolling tag detected (bitnami/nginx-exporter:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
```

## Wait for Bitnami Nginx readiness; detect unavailable image.

Exit code: 0

```text
Waiting for deployment "my-nginx" rollout to finish: 0 of 1 updated replicas are available...
deployment "my-nginx" successfully rolled out
```

## Diagnose chart image availability.

Exit code: 0

```text
NAME                        READY   STATUS    RESTARTS   AGE
my-nginx-67c767ddc4-ncxg6   1/1     Running   0          39s
14s         Normal   Started     pod/my-nginx-67c767ddc4-ncxg6     Container started
12s         Normal   Pulled      pod/my-nginx-67c767ddc4-ncxg6     Container image "registry-1.docker.io/bitnami/nginx:latest" already present on machine and can be accessed by the pod
9s          Normal   Created     pod/my-nginx-67c767ddc4-ncxg6     Container created
9s          Normal   Scheduled   pod/web-2                         Successfully assigned default/web-2 to devops-cluster-control-plane
8s          Normal   Started     pod/my-nginx-67c767ddc4-ncxg6     Container started
8s          Normal   Started     pod/web-2                         Container started
8s          Normal   Created     pod/web-2                         Container created
8s          Normal   Pulled      pod/web-2                         Container image "nginx:1.25" already present on machine and can be accessed by the pod
3s          Normal   Scheduled   pod/stateful-dns                  Successfully assigned default/stateful-dns to devops-cluster-control-plane
2s          Normal   Started     pod/stateful-dns                  Container started
2s          Normal   Pulled      pod/stateful-dns                  Container image "busybox:1.36" already present on machine and can be accessed by the pod
2s          Normal   Created     pod/stateful-dns                  Container created
```

## Inspect rendered release manifests in temporary storage.

Exit code: 0

```text

```

## Install custom chart and wait for readiness.

Exit code: 0

```text
NAME: my-release
LAST DEPLOYED: Wed Sep 30 13:34:41 2026
NAMESPACE: default
STATUS: deployed
REVISION: 1
DESCRIPTION: Install complete
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=my-app,app.kubernetes.io/instance=my-release" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

## Verify custom chart has three ready replicas.

Exit code: 0

```text
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
my-release-my-app   3/3     3            3           4s
```

## Upgrade custom chart to five replicas.

Exit code: 0

```text
Release "my-release" has been upgraded. Happy Helming!
NAME: my-release
LAST DEPLOYED: Wed Sep 30 13:34:49 2026
NAMESPACE: default
STATUS: deployed
REVISION: 2
DESCRIPTION: Upgrade complete
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=my-app,app.kubernetes.io/instance=my-release" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

## Verify custom release upgrade and revision history.

Exit code: 0

```text
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
my-release-my-app   5/5     5            5           13s
REVISION	UPDATED                 	STATUS    	CHART       	APP VERSION	DESCRIPTION
1       	Wed Sep 30 13:34:41 2026	superseded	my-app-0.1.0	1.16.0     	Install complete
2       	Wed Sep 30 13:34:49 2026	deployed  	my-app-0.1.0	1.16.0     	Upgrade complete
```

## Install customized release with three replicas and NodePort via --set.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
NAME: nginx-cli
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
CHART NAME: nginx
? WARNING: Since August 28th, 2025, only a limited subset of images/charts are available for free.
** Please be patient while the chart is being deployed **
WARNING: Rolling tag detected (bitnami/nginx:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: Rolling tag detected (bitnami/git:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: Rolling tag detected (bitnami/nginx-exporter:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
```

## Install values-file release with resource requests and limits.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
NAME: nginx-values
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
CHART NAME: nginx
? WARNING: Since August 28th, 2025, only a limited subset of images/charts are available for free.
** Please be patient while the chart is being deployed **
WARNING: Rolling tag detected (bitnami/nginx:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: Rolling tag detected (bitnami/git:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: Rolling tag detected (bitnami/nginx-exporter:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
```

## Verify values, three ready replicas and NodePort Service.

Exit code: 0

```text
USER-SUPPLIED VALUES:
replicaCount: 3
resources:
  limits:
    cpu: 250m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi
service:
  type: NodePort
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
nginx-values   3/3     3            3           10s
NAME           TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
nginx-values   NodePort   10.96.241.111   <none>        80:32339/TCP,443:31740/TCP   11s
```

## Upgrade original Bitnami release to five replicas.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
NAME: my-nginx
NAMESPACE: default
STATUS: deployed
REVISION: 2
TEST SUITE: None
CHART NAME: nginx
? WARNING: Since August 28th, 2025, only a limited subset of images/charts are available for free.
** Please be patient while the chart is being deployed **
  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
WARNING: Rolling tag detected (bitnami/nginx:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: Rolling tag detected (bitnami/git:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: Rolling tag detected (bitnami/nginx-exporter:latest), please note that it is strongly recommended to avoid using rolling tags in a production environment.
WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
```

## Verify upgraded replicas and two history entries.

Exit code: 0

```text
NAME       READY   UP-TO-DATE   AVAILABLE   AGE
my-nginx   5/5     5            5           3m36s
REVISION	UPDATED                 	STATUS    	CHART       	APP VERSION	DESCRIPTION
1       	Wed Sep 30 13:33:53 2026	superseded	nginx-25.2.1	1.31.6     	Install complete
2       	Wed Sep 30 13:37:09 2026	deployed  	nginx-25.2.1	1.31.6     	Upgrade complete
```

## Restore original release values as a new revision.

Exit code: 0

```text
Rollback was a success! Happy Helming!
```

## Verify rollback to one replica and revision three.

Exit code: 0

```text
NAME       READY   UP-TO-DATE   AVAILABLE   AGE
my-nginx   1/1     1            1           3m40s
REVISION	UPDATED                 	STATUS    	CHART       	APP VERSION	DESCRIPTION
1       	Wed Sep 30 13:33:53 2026	superseded	nginx-25.2.1	1.31.6     	Install complete
2       	Wed Sep 30 13:37:09 2026	superseded	nginx-25.2.1	1.31.6     	Upgrade complete
3       	Wed Sep 30 13:37:35 2026	deployed  	nginx-25.2.1	1.31.6     	Rollback to 1
```

## Run generated custom-chart HTTP connectivity test.

Exit code: 0

```text
NAME: my-release
LAST DEPLOYED: Wed Sep 30 13:34:49 2026
NAMESPACE: default
STATUS: deployed
REVISION: 2
DESCRIPTION: Upgrade complete
TEST SUITE:     my-release-my-app-test-connection
Last Started:   Wed Sep 30 13:37:38 2026
Last Completed: Wed Sep 30 13:39:05 2026
Phase:          Succeeded

POD LOGS: my-release-my-app-test-connection (wget)
Connecting to my-release-my-app:80 (10.96.190.196:80)
saving to 'index.html'
index.html           100% |********************************|   615  0:00:00 ETA
'index.html' saved
```

## Uninstall all four newly created exercise releases. Deletes exercise resources; approval required.

Exit code: 0

```text
release "my-nginx" uninstalled
release "nginx-cli" uninstalled
release "nginx-values" uninstalled
release "my-release" uninstalled
```

## Verify no Helm releases remain; other running days may still have workloads.

Exit code: 0

```text
NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   56d
```

## Remove generated Helm test hook, which can outlive uninstall. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "my-release-my-app-test-connection" deleted from default namespace
```

## Verify no Helm releases or application Pods remain in default.

Exit code: 0

```text
NAME	NAMESPACE	REVISION	UPDATED	STATUS	CHART	APP VERSION
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   56d
```

## Validate final chart metadata, lint and rendered resources after matching appVersion to nginx:1.25.

Exit code: 0

```text
==> Linting my-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
serviceaccount/my-release-my-app created (server dry run)
service/my-release-my-app created (server dry run)
deployment.apps/my-release-my-app created (server dry run)
pod/my-release-my-app-test-connection created (server dry run)
```
