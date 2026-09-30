# Day 84 Tasks

Run from this day's directory in WSL Bash. Commands with placeholders require replacement. Cloud steps are pending where credentials are unavailable. Cleanup deletes disposable resources/data and must target only the reviewed lab.

| Command | What it does |
| --- | --- |
| `mkdir -p .runtime` | Create the private directory. |
| `kind create cluster --name days81-90-lab --image kindest/node:v1.36.1 --kubeconfig .runtime/kubeconfig --wait 120s` | Local alternative: create a dedicated disposable cluster and private kubeconfig. |
| `export KUBECONFIG="$PWD/.runtime/kubeconfig"` | Select the disposable cluster; preserve the existing default kubeconfig. |
| `helm upgrade --install argocd argo-cd --version 10.9.5 --repo https://argoproj.github.io/argo-helm -n argocd --create-namespace --set configs.params.server.insecure=true --wait --timeout 300s` | Local loopback-only ArgoCD installation; record the resolved chart version in validation.md. |
| `python3 create-lab-secret.py` | Create namespace and random credentials while preserving an existing Secret. |
| `kubectl apply --dry-run=server -f local-application.yaml; kubectl apply -f local-application.yaml` | Local alternative: validate and deploy the prior chart from the public Git repository. |
| `kubectl apply --dry-run=server -f application.yaml; kubectl apply -f application.yaml` | EKS alternative only, after sanitizing/forking source and installing required EBS/Gateway/cert-manager APIs. |
| `kubectl get application,pods -n argocd; kubectl get pods,pvc -n bankapp-local` | Inspect sync/health separately and check app readiness. |
| `kubectl port-forward svc/argocd-server -n argocd 8443:443` | Loopback UI access; retrieve credentials privately and stop with Ctrl-C. |
| `argocd login localhost:8443 --username admin --insecure` | If CLI is installed, prompt for credentials privately; insecure is only for the local self-signed endpoint. |
| `argocd app get bankapp; argocd app wait bankapp --timeout 600; argocd app history bankapp` | Required EKS exercise: inspect status, bounded readiness wait and sync history. |
| `kubectl scale deployment bankapp-local-bankapp -n bankapp-local --replicas=2` | Local disposable drift test without HPA: observe ArgoCD restore the Git value. |
| `kubectl delete configmap bankapp-local-bankapp-config -n bankapp-local` | Destructive local-only drift test: observe controller recreation. |
| `python3 validate-gitops.py` | Run the recorded HTTP, scale, ConfigMap and manual-sync checks in the disposable lab; requires the day-82 local Gateway. |
| `kubectl delete application bankapp-local -n argocd` | Remove the local Application; this alternative has no cascading finalizer. |
| `kind delete cluster --name days81-90-lab` | Destructive cleanup after Days 84-89 checks: remove only the task-created cluster and its disposable data. |
