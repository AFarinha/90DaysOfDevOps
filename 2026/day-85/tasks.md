# Day 85 Tasks

Run from this day's directory in WSL Bash. Commands with placeholders require replacement. Cloud steps are pending where credentials are unavailable. Cleanup deletes disposable resources/data and must target only the reviewed lab.

| Command | What it does |
| --- | --- |
| `export KUBECONFIG="$PWD/../day-84/.runtime/kubeconfig"` | Select the isolated local lab for API validation; use the EKS kubeconfig for cloud exercise. |
| `python3 prepare-sync-waves.py ../day-81/.runtime/AI-BankApp-DevOps/k8s` | Generate wave annotations in ignored local output; excludes plaintext Secrets and environment-specific Gateway/TLS resources. |
| `argocd app set bankapp --sync-policy none; argocd app diff bankapp; argocd app sync bankapp --dry-run` | Switch to manual, inspect drift and preview before applying; CLI authentication required. |
| `argocd app sync bankapp; argocd app set bankapp --sync-policy automated --self-heal --auto-prune` | Manual apply then restore automation; pruning may remove data-bearing objects. |
| `argocd app history bankapp` | Find a real historical revision; do not assume the README's sample ID exists. |
| `argocd app set bankapp --sync-policy none; argocd app rollback bankapp <verified-history-id>` | Deployment mutation: disable automation and select an actual successful revision. |
| `git revert <reviewed-commit>; git push origin feat/gitops` | In the owned app fork only: create and publish a reviewed rollback commit; these commands were not executed. |
| `kubectl apply --dry-run=server -f root-app.yaml -f project-rbac.yaml -f notifications.yaml -f argocd-apps` | Validate ArgoCD/configuration schemas without executing the cloud apps. |
| `kubectl apply -f root-app.yaml` | After publishing sanitized children to the watched Git path, bootstrap App of Apps. |
| `kubectl apply -f project-rbac.yaml; argocd app set bankapp --project bankapp-team` | Apply source/destination limits and assign the app; update source allowlist when using a personal fork. |
| `kubectl apply -f notifications.yaml` | Configure webhook delivery only after supplying the private endpoint Secret. |
| `kubectl annotate application bankapp -n argocd notifications.argoproj.io/subscribe.on-sync-succeeded.lab='' notifications.argoproj.io/subscribe.on-sync-failed.lab='' notifications.argoproj.io/subscribe.on-health-degraded.lab='' --overwrite` | Subscribe to the named lab webhook; only use an explicitly approved receiver. |
| `argocd app set root-app --sync-policy none; argocd app delete root-app; argocd app delete bankapp --cascade` | Destructive cleanup: stop the parent recreating children, then delete exact managed apps after data review. |
