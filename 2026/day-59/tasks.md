# Day 59 Tasks

Run from `2026/day-59/` using Bash in WSL and context `kind-devops-cluster`. Commands are listed in execution order. Start with `export PATH="$HOME/.local/bin:$PATH"` to expose user-local tools. `-n` selects a namespace, `-A` selects all namespaces, and `-f` reads a manifest. Dry-runs validate without persisting; `--wait` and `--timeout` bound readiness waits. Deletion commands affect only exercise resources and require approval.

| Command | What it does |
| --- | --- |
| `curl -fsSL https://get.helm.sh/helm-v4.3.0-linux-amd64.tar.gz -o /tmp/day59-helm.tar.gz` | Download official Helm v4.3.0 archive into temporary storage. |
| `curl -fsSL https://get.helm.sh/helm-v4.3.0-linux-amd64.tar.gz.sha256sum -o /tmp/day59-helm.sha256sum` | Download the official archive checksum. |
| `python3 -c 'import hashlib,pathlib; p=pathlib.Path("/tmp/day59-helm.tar.gz"); expected=pathlib.Path("/tmp/day59-helm.sha256sum").read_text().split()[0]; assert hashlib.sha256(p.read_bytes()).hexdigest()==expected; print("Helm checksum verified")'` | Verify SHA256 against the downloaded official checksum. |
| `mkdir -p /tmp/day59-helm && tar -xzf /tmp/day59-helm.tar.gz -C /tmp/day59-helm && install -m 755 /tmp/day59-helm/linux-amd64/helm "$HOME/.local/bin/helm"` | Extract and install Helm in ~/.local/bin without sudo. |
| `export PATH="$HOME/.local/bin:$PATH"; helm version --short` | Make user-local tools available in Bash and verify Helm version. |
| `helm env` | Inspect Helm configuration paths. |
| `helm repo add bitnami https://charts.bitnami.com/bitnami` | Add Bitnami chart repository. |
| `helm repo update` | Refresh chart repository index. |
| `helm search repo nginx` | Search available Nginx charts. |
| `helm search repo bitnami -o json \| python3 -c 'import json,sys; print("Bitnami chart count:",len(json.load(sys.stdin)))'` | Count Bitnami charts without listing full index. |
| `helm show chart bitnami/nginx` | Verify chart version and application version. |
| `helm show values bitnami/nginx > /tmp/day59-nginx-default-values.yaml` | Inspect defaults via a temporary file; avoid duplicating the full chart values. |
| `helm create my-app` | Scaffold the custom application chart. |
| `helm lint my-app` | Validate chart structure and templates. |
| `helm template my-release ./my-app > /tmp/day59-rendered.yaml` | Render custom chart without installation. |
| `kubectl apply --dry-run=client -f /tmp/day59-rendered.yaml; kubectl apply --dry-run=server -f /tmp/day59-rendered.yaml` | Validate rendered manifests locally and on API server. |
| `helm install my-nginx bitnami/nginx --version 25.2.1` | Install pinned Bitnami Nginx chart. |
| `kubectl get all -l app.kubernetes.io/instance=my-nginx; helm list; helm status my-nginx` | Inspect chart resources and release status. |
| `kubectl rollout status deployment/my-nginx --timeout=90s` | Wait for Bitnami Nginx readiness; detect unavailable image. |
| `kubectl get pods -l app.kubernetes.io/instance=my-nginx; kubectl get events --field-selector involvedObject.kind=Pod --sort-by=.lastTimestamp \| tail -12` | Diagnose chart image availability. |
| `helm get manifest my-nginx > /tmp/day59-bitnami-manifest.yaml` | Inspect rendered release manifests in temporary storage. |
| `helm install my-release ./my-app --wait --timeout=180s` | Install custom chart and wait for readiness. |
| `kubectl get deployment my-release-my-app` | Verify custom chart has three ready replicas. |
| `helm upgrade my-release ./my-app --set replicaCount=5 --wait --timeout=180s` | Upgrade custom chart to five replicas. |
| `kubectl get deployment my-release-my-app; helm history my-release` | Verify custom release upgrade and revision history. |
| `helm install nginx-cli bitnami/nginx --version 25.2.1 --set replicaCount=3 --set service.type=NodePort --wait --timeout=180s` | Install customized release with three replicas and NodePort via --set. |
| `helm install nginx-values bitnami/nginx --version 25.2.1 -f custom-values.yaml --wait --timeout=180s` | Install values-file release with resource requests and limits. |
| `helm get values nginx-values; kubectl get deployment nginx-values; kubectl get service nginx-values` | Verify values, three ready replicas and NodePort Service. |
| `helm upgrade my-nginx bitnami/nginx --version 25.2.1 --set replicaCount=5 --wait --timeout=180s` | Upgrade original Bitnami release to five replicas. |
| `kubectl get deployment my-nginx; helm history my-nginx` | Verify upgraded replicas and two history entries. |
| `helm rollback my-nginx 1 --wait --timeout=180s` | Restore original release values as a new revision. |
| `kubectl get deployment my-nginx; helm history my-nginx` | Verify rollback to one replica and revision three. |
| `helm test my-release --logs` | Run generated custom-chart HTTP connectivity test. |
| `helm uninstall my-nginx nginx-cli nginx-values my-release` | Uninstall all four newly created exercise releases. Deletes exercise resources; approval required. |
| `helm list; kubectl get deployments,services` | Verify no Helm releases remain; other running days may still have workloads. |
| `kubectl delete pod my-release-my-app-test-connection -n default --ignore-not-found` | Remove generated Helm test hook, which can outlive uninstall. Deletes exercise resources; approval required. |
| `helm list -n default; kubectl get pods,services -n default` | Verify no Helm releases or application Pods remain in default. |
| `helm lint my-app; helm template my-release ./my-app > /tmp/day59-rendered.yaml; kubectl apply --dry-run=server -n default -f /tmp/day59-rendered.yaml` | Validate final chart metadata, lint and rendered resources after matching appVersion to nginx:1.25. |

The included `my-app` chart is already configured. Skip `helm create my-app` when the directory exists; scaffolding is only for a fresh directory. For a new scaffold, set `values.yaml` to `replicaCount: 3`, `image.repository: nginx`, `image.tag: "1.25"`, and `Chart.yaml` to `appVersion: "1.25"` before linting or installing. Keep the chart and `custom-values.yaml` as source deliverables.

## Submission

The README requires commit and push to the fork. Run from the repository root after validation; stage only this day. Push publishes the committed work to origin/master.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-59/` | Stage only this day; do not include unrelated AGENTS.md. |
| `git commit -m "Day 59 - Completed - Deploy customize and roll back Helm charts"` | Create the required completion commit. |
| `git push origin master` | Publish completion commits to the fork; changes the remote branch. |
