# Day 78 Commands

Run from this day directory. Choose the existing-cluster route or create the optional isolated cluster; do not blindly switch contexts. Cleanup is destructive only to disposable lab resources.

| Command | What it does |
| --- | --- |
| `kubectl cluster-info` | Confirm the selected cluster before creating the lab namespace. |
| `kubectl create namespace days71-80-lab` | Create isolated namespace once; omit if already created by this lab. |
| `python3 create-lab-secret.py days71-80-lab` | Create random existing Secret privately, or preserve one that already exists. |
| `kind create cluster --config kind-config.yml` | Alternative to using the existing cluster: creates a separate three-node cluster; requires downloading its node image. |
| `helm repo add bitnami https://charts.bitnami.com/bitnami` | Add MySQL chart repository; omit if already configured. |
| `helm repo update bitnami` | Refresh public chart metadata. |
| `helm search repo bitnami/mysql` | Discover available MySQL charts. |
| `helm pull bitnami/mysql --version 14.0.3 --untar --untardir .cache` | Retrieve verified chart version into an ignored local cache. |
| `helm show values .cache/mysql` | Inspect all configuration options; output includes upstream example/default values. |
| `helm install bankapp-mysql .cache/mysql -f mysql-values.yaml -n days71-80-lab` | Install first MySQL release using a private existing Secret. |
| `helm install bankapp-mysql-v2 .cache/mysql -f mysql-values.yaml -n days71-80-lab` | Optional second release for values-file practice; both need runnable images. |
| `helm repo add nginx https://helm.nginx.com/stable` | Add the official NGINX chart repository. |
| `helm install lab-nginx nginx/nginx-ingress --version 2.7.3 -n days71-80-lab --set controller.service.type=ClusterIP` | Install a second application without exposing a host LoadBalancer. |
| `helm list -n days71-80-lab` | List releases; deployed status alone is not a readiness check. |
| `kubectl get pods,pvc -n days71-80-lab` | Inspect workloads and storage without revealing Secrets. |
| `helm upgrade bankapp-mysql .cache/mysql -f mysql-values.yaml -n days71-80-lab --set metrics.enabled=false` | Create a new revision by disabling metrics; retain Secret/database/persistence values. |
| `helm history bankapp-mysql -n days71-80-lab` | Inspect revision history. |
| `helm rollback bankapp-mysql 1 -n days71-80-lab` | Create a rollback revision from revision 1. |
| `helm upgrade bankapp-mysql .cache/mysql -f mysql-values.yaml -n days71-80-lab --set image.repository=bitnamilegacy/mysql --set metrics.image.repository=bitnamilegacy/mysqld-exporter --set global.security.allowInsecureImages=true` | Lab-only archived-image alternative if default images are unavailable. These images have no ongoing update guarantee. |
| `kubectl exec -n days71-80-lab bankapp-mysql-0 -- bash -lc 'MYSQL_PWD="${MYSQL_ROOT_PASSWORD:-$(cat "$MYSQL_ROOT_PASSWORD_FILE")}" mysql -uroot -e "SHOW DATABASES;"'` | Verify bankappdb without printing the password; requires a Ready database. |
| `helm uninstall bankapp-mysql bankapp-mysql-v2 lab-nginx -n days71-80-lab` | Cleanup: remove only lab releases that exist; release uninstall may leave StatefulSet PVCs. |
| `kubectl delete namespace days71-80-lab` | Destructive cleanup: delete the disposable lab namespace and its storage. Never use for a namespace with real data. |
| `kind delete cluster --name days71-80-lab` | Only if this task created the optional cluster; never delete the existing devops-cluster. |
