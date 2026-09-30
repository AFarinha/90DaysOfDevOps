# Day 80 Commands

Run from this day directory. Use one dedicated namespace/release name and preserve existing Secrets and PVC sizes on upgrade. `.runtime` is ignored. Full AI deployment and the dev alternative have different validation scope.

| Command | What it does |
| --- | --- |
| `kubectl create namespace days71-80-lab` | First run only: create the disposable namespace, preserving the existing cluster. |
| `python3 create-lab-secret.py days71-80-lab` | Create random credentials privately; preserve an existing Secret. |
| `helm lint bankapp` | Validate chart syntax and structure. |
| `helm template my-bankapp bankapp -n days71-80-lab` | Render manifests without installing; avoid printing real generated Secret values. |
| `helm template my-bankapp bankapp -n days71-80-lab --set ollama.enabled=false,mysql.enabled=false,config.externalMysqlHost=external-db.example.com,bankapp.autoscaling.enabled=false,bankapp.replicaCount=2` | Validate optional resources and fixed replicas using a placeholder external database. |
| `helm template my-bankapp bankapp -n days71-80-lab > .runtime/rendered.yaml` | Save rendered manifests in private ignored storage; create .runtime first if needed. |
| `kubectl apply --dry-run=server -f .runtime/rendered.yaml` | Ask the API server to validate without persisting resources. |
| `helm install my-bankapp bankapp -n days71-80-lab --wait --timeout 600s` | Deploy full MySQL/Ollama/app stack; downloads images/model and writes disposable PVC data. |
| `kubectl get deployment,pod,service,pvc -n days71-80-lab` | Inspect readiness, services and storage. |
| `kubectl port-forward -n days71-80-lab svc/my-bankapp-bankapp-service 18079:8080` | Foreground loopback access; stop with Ctrl-C after testing. |
| `curl --fail http://127.0.0.1:18079/actuator/health` | Verify the application through the forwarded service. |
| `mkdir -p .runtime` | Create ignored local directory for packages/rendered output. |
| `helm package bankapp --destination .runtime` | Build a distributable package without adding its binary archive to Git. |
| `helm lint bankapp -f bankapp/values-dev.yaml` | Validate dev configuration; repeat with staging/prod files for those environments. |
| `helm template bankapp-staging bankapp -f bankapp/values-staging.yaml` | Render staging without touching a cloud cluster. |
| `helm template bankapp-prod bankapp -f bankapp/values-prod.yaml` | Render production; requires CSI/Gateway APIs if actually deployed. |
| `helm upgrade --install my-bankapp bankapp -f bankapp/values-dev.yaml -n days71-80-lab --set bankapp.image.tag=1c7cb0e --set ollama.enabled=false --wait --timeout 300s --atomic` | Fresh-release dev alternative without AI; atomic rolls back failures. Preserve existing PVC size on upgrades. |
| `helm test my-bankapp -n days71-80-lab --timeout 120s` | Run HTTP health test after a successful deployment. |
| `helm repo index .runtime --url https://example.com/helm-charts` | Generate local repository metadata; placeholder URL does not publish anything. |
| `helm list -A` | Inspect releases across namespaces without altering them. |
| `helm uninstall my-bankapp -n days71-80-lab` | Cleanup this exact lab release; use actual chosen lab name if different. |
| `kubectl delete namespace days71-80-lab` | Destructive cleanup: delete only disposable lab storage/resources after all three days. Preserve the existing cluster. |
