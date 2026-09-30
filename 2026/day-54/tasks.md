# Day 54 Tasks

Run from `2026/day-54/` using Bash in WSL and context `kind-devops-cluster`. Commands are listed in execution order. Start with `export PATH="$HOME/.local/bin:$PATH"` to expose user-local tools. `-n` selects a namespace, `-A` selects all namespaces, and `-f` reads a manifest. Dry-runs validate without persisting; `--wait` and `--timeout` bound readiness waits. Deletion commands affect only exercise resources and require approval.

| Command | What it does |
| --- | --- |
| `kubectl create configmap app-config --from-literal=APP_ENV=production --from-literal=APP_DEBUG=false --from-literal=APP_PORT=8080` | Create plaintext config from literals. |
| `kubectl describe configmap app-config; kubectl get configmap app-config -o yaml` | Verify configuration keys. |
| `kubectl create configmap nginx-config --from-file=default.conf=default.conf` | Create file-backed ConfigMap. |
| `kubectl get configmap nginx-config -o yaml` | Inspect Nginx configuration. |
| `kubectl apply --dry-run=client -f config-env-pod.yaml` | Validate config-env-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f config-env-pod.yaml` | Validate config-env-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f config-env-pod.yaml` | Apply config-env-pod.yaml. |
| `kubectl apply --dry-run=client -f nginx-config-pod.yaml` | Validate nginx-config-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f nginx-config-pod.yaml` | Validate nginx-config-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f nginx-config-pod.yaml` | Apply nginx-config-pod.yaml. |
| `kubectl wait --for=condition=Ready pod/config-env pod/config-nginx --timeout=180s` | Wait for exercise Pods to become Ready (180-second timeout). |
| `kubectl logs config-env; kubectl exec config-nginx -- curl -fsS http://localhost/health` | Verify environment injection and health response. |
| `DB_PASSWORD=$(python3 -c 'import secrets; print(secrets.token_urlsafe(24))'); export DB_PASSWORD; kubectl create secret generic db-credentials --from-literal=DB_USER=admin --from-literal=DB_PASSWORD="$DB_PASSWORD"` | Generate temporary password in memory and create Secret without printing it. |
| `kubectl apply --dry-run=client -f secret-pod.yaml` | Validate secret-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f secret-pod.yaml` | Validate secret-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f secret-pod.yaml` | Apply secret-pod.yaml. |
| `kubectl wait --for=condition=Ready pod/secret-consumer --timeout=180s` | Wait for exercise Pods to become Ready (180-second timeout). |
| `kubectl exec secret-consumer -- sh -c 'test "$DB_USER" = admin && test "$(cat /etc/db-credentials/DB_USER)" = admin && test -s /etc/db-credentials/DB_PASSWORD && echo "Secret env and plaintext files verified; password not printed"'` | Verify Secret env and plaintext mounted files. |
| `kubectl get secret db-credentials -o json \| python3 -c 'import sys,json,base64; d=json.load(sys.stdin)["data"]; assert base64.b64decode(d["DB_USER"])==b"admin"; assert len(base64.b64decode(d["DB_PASSWORD"]))>0; print("Base64 decoding verified without printing credentials")'` | Decode Secret in memory to verify encoding. |
| `kubectl create configmap live-config --from-literal=message=hello` | Create live configuration. |
| `kubectl apply --dry-run=client -f live-config-pod.yaml` | Validate live-config-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f live-config-pod.yaml` | Validate live-config-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f live-config-pod.yaml` | Apply live-config-pod.yaml. |
| `kubectl wait --for=condition=Ready pod/live-config-reader --timeout=180s` | Wait for exercise Pods to become Ready (180-second timeout). |
| `kubectl patch configmap live-config --type merge -p '{"data":{"message":"world"}}'` | Update message with JSON merge patch. |
| `for attempt in {1..30}; do value=$(kubectl exec live-config-reader -- cat /config/message); [ "$value" = world ] && break; sleep 5; done; test "$value" = world; kubectl get pod live-config-reader; kubectl logs live-config-reader --tail=6` | Wait up to 150 seconds for volume propagation; verify no restart. |
| `kubectl delete -f config-env-pod.yaml -f nginx-config-pod.yaml -f secret-pod.yaml -f live-config-pod.yaml; kubectl delete configmap app-config nginx-config live-config; kubectl delete secret db-credentials` | Remove Pods, ConfigMaps and temporary Secret. Deletes exercise resources; approval required. |

## Submission

The README requires commit and push to the fork. Run from the repository root after validation; stage only this day. Push publishes the committed work to origin/master.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-54/` | Stage only this day; do not include unrelated AGENTS.md. |
| `git commit -m "Day 54 - Completed - Consume ConfigMaps and Secrets securely"` | Create the required completion commit. |
| `git push origin master` | Publish completion commits to the fork; changes the remote branch. |
