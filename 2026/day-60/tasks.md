# Day 60 Tasks

Run from `2026/day-60/` in Bash/WSL. Commands follow the corrected exercise order. Fresh namespaces must not collide with existing work. `-n` selects namespace, `-f` reads a manifest, and `--timeout` bounds readiness waits. The final port-forward row is an access alternative, not a command to run after deleting the stack.

| Command | What it does |
| --- | --- |
| `export PATH="$HOME/.local/bin:$PATH"` | Expose the user-local kubectl and Helm tools in Bash. |
| `kubectl config current-context; kubectl get nodes; kubectl get storageclass` | Verify kind-devops-cluster, Ready node and standard StorageClass before applying. |
| `kubectl apply --dry-run=client -f namespace.yaml; kubectl apply --dry-run=server -f namespace.yaml; kubectl apply -f namespace.yaml` | Validate and create the capstone namespace. Dry-runs do not persist resources. |
| `kubectl config set-context --current --namespace=capstone` | Change the current context default namespace for the exercise; restore it during cleanup. |
| `export MYSQL_ROOT_PASSWORD=$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))'); export MYSQL_PASSWORD=$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))'); python3 create-secret.py` | Generate temporary credentials in memory; script performs client/server dry-runs and applies Secret stringData without printing it. For an existing initialized database, reuse its credentials rather than rotating blindly. |
| `for file in mysql-service.yaml mysql-statefulset.yaml wordpress-configmap.yaml wordpress-deployment.yaml wordpress-service.yaml; do kubectl apply --dry-run=client -f "$file" && kubectl apply --dry-run=server -f "$file" && kubectl apply -f "$file" \|\| break; done` | Validate each manifest locally and on the server before applying. Stop on the first failure; fix it before continuing. |
| `kubectl rollout status statefulset/mysql -n capstone --timeout=300s; kubectl rollout status deployment/wordpress -n capstone --timeout=300s` | Wait for database and both WordPress replicas; allow initial image download and initialization. |
| `kubectl exec mysql-0 -n capstone -- sh -c 'MYSQL_PWD="$MYSQL_PASSWORD" mysql -u "$MYSQL_USER" -e "SHOW DATABASES;"'` | Verify wordpress database using credentials already in the container environment. |
| `kubectl get all,pvc -n capstone` | Inspect Pods, controllers, Services and storage. get all does not include every resource type. |
| `export WORDPRESS_URL="http://$(kubectl get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}'):30080"` | Set the NodePort URL reachable from WSL; the tested node IP was 172.18.0.2. |
| `export WORDPRESS_ADMIN_PASSWORD=$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))'); python3 setup-wordpress.py` | Complete the fresh site HTTP installation wizard. Keep the disposable password only in memory; do not print it. |
| `kubectl exec -n capstone deployment/wordpress -- php -r 'require "/var/www/html/wp-load.php"; $id=wp_insert_post(["post_title"=>"Day 60 persistence proof","post_content"=>"This post must survive WordPress and MySQL Pod replacement.","post_status"=>"publish"]); if (!$id \|\| is_wp_error($id)) { exit(1); } echo "Published test post ID: ".$id.PHP_EOL;'` | Publish a local test blog post through the application API and record its ID; repeating creates another post. |
| `curl -fsS "$WORDPRESS_URL/" \| python3 -c 'import sys; assert "Day 60 persistence proof" in sys.stdin.read(); print("Published post visible")'` | Require successful HTTP and verify the published post content. Repeat after each recovery test. |
| `pod=$(kubectl get pods -n capstone -l app=wordpress -o jsonpath='{.items[0].metadata.name}'); kubectl delete pod "$pod" -n capstone` | Delete one test WordPress Pod to exercise recovery; requires approval. |
| `kubectl rollout status deployment/wordpress -n capstone --timeout=180s` | Wait for WordPress recovery, then repeat the HTTP check. |
| `kubectl delete pod mysql-0 -n capstone; kubectl wait --for=condition=Ready pod/mysql-0 -n capstone --timeout=180s` | Delete database Pod, retain PVC and wait for recovery; requires approval. Repeat the HTTP check. |
| `kubectl exec mysql-0 -n capstone -- sh -c 'MYSQL_PWD="$MYSQL_PASSWORD" mysql -u "$MYSQL_USER" wordpress -e "SELECT ID, post_title, post_status FROM wp_posts;"'` | Verify the same post ID/title/status persists without exposing the database password. |
| `kubectl apply --dry-run=client -f wordpress-hpa.yaml; kubectl apply --dry-run=server -f wordpress-hpa.yaml; kubectl apply -f wordpress-hpa.yaml` | Validate and apply HPA only after initialization and persistence checks. |
| `kubectl get hpa -n capstone; kubectl describe hpa wordpress -n capstone` | Verify numeric CPU target, minimum two and maximum ten; wait for metrics if initially unknown. |
| `helm install wp-helm bitnami/wordpress --version 34.1.1 --namespace capstone-helm --create-namespace --wait --timeout=300s` | Optional bonus: install the verified chart in a new separate namespace, with a five-minute readiness budget. |
| `kubectl get all,pvc -n capstone-helm; helm list -n capstone-helm` | Compare the chart deployment, which uses MariaDB and persists WordPress files. |
| `for ns in capstone capstone-helm; do kubectl get deployment,statefulset,service,configmap,secret,pvc,hpa -n "$ns" -o name \| wc -l; done` | Count the same selected resource types in each namespace. Counts include bootstrap ConfigMap and Helm release Secret. |
| `helm uninstall wp-helm -n capstone-helm; kubectl delete namespace capstone-helm` | Remove bonus release and namespace including retained storage; deletes test data and requires approval. |
| `kubectl delete namespace capstone` | Delete all manual resources and claims; dynamic Delete policy removes database storage. Destructive: requires approval after evidence is recorded. |
| `kubectl config set-context --current --namespace=default; unset MYSQL_ROOT_PASSWORD MYSQL_PASSWORD WORDPRESS_ADMIN_PASSWORD WORDPRESS_URL` | Restore namespace and clear disposable credentials from the current shell. |
| `kubectl get namespaces; kubectl get pvc -A; kubectl get pv; helm list -A; kubectl get all -A` | Verify no exercise resources remain and Metrics Server stays installed. |
| `kubectl port-forward svc/wordpress 8080:80 -n capstone` | Alternative access while stack exists: run in another terminal, use WORDPRESS_URL=http://127.0.0.1:8080 and stop with Ctrl+C before cleanup. |
| `kubectl get namespaces; kubectl get pods,services -n default; kubectl get pvc -A; kubectl get pv; helm list -A; kubectl get deployment metrics-server -n kube-system` | Verify final cleanup: no exercise namespaces, Pods, claims, volumes or Helm releases; Metrics Server is retained. |

## Submission

The README requires commit and push to the fork. Run from the repository root after validation; stage only this day. Push publishes the committed work to origin/master.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-60/` | Stage only this day; do not include unrelated AGENTS.md. |
| `git commit -m "Day 60 - Completed - Deploy and validate WordPress MySQL capstone"` | Create the required completion commit. |
| `git push origin master` | Publish completion commits to the fork; changes the remote branch. |
