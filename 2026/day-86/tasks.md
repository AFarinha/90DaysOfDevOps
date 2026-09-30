# Day 86 Tasks

Run from this day's directory in WSL Bash. Commands with placeholders require replacement. Cloud steps are pending where credentials are unavailable. Cleanup deletes disposable resources/data and must target only the reviewed lab.

| Command | What it does |
| --- | --- |
| `export KUBECONFIG="$PWD/../day-81/.runtime/eks-kubeconfig"` | Select verified EKS context after AWS provisioning. |
| `gh repo fork TrainWithShubham/AI-BankApp-DevOps --clone=false` | Required exercise preparation: create an owned fork; not executed in this credential-blocked run. |
| `gh secret set DOCKERHUB_USERNAME --repo <owner>/AI-BankApp-DevOps; gh secret set DOCKERHUB_TOKEN --repo <owner>/AI-BankApp-DevOps` | Prompt privately for registry credentials; never place values in documentation. |
| `gh variable set DOCKERHUB_REPO --repo <owner>/AI-BankApp-DevOps --body <owned-registry-repository>` | Configure the owned registry namespace. |
| `cp gitops-ci.yml <owned-app-checkout>/.github/workflows/gitops-ci.yml` | Copy the reviewed workflow into the fork checkout after replacing placeholders. |
| `git add .github/workflows/gitops-ci.yml src/ k8s/bankapp-deployment.yml; git commit -m 'Day 86 - Completed - Configure BankApp GitOps pipeline'; git push origin feat/gitops` | In the owned checkout only: publish the pipeline/source change and trigger image publishing. Not run here. |
| `gh run list --repo <owner>/AI-BankApp-DevOps --limit 5; gh run watch <run-id> --repo <owner>/AI-BankApp-DevOps` | Inspect a real CI run, using its returned ID. |
| `argocd app get bankapp --refresh; argocd app wait bankapp --timeout 600` | Wait for the actual bot manifest commit to roll out. |
| `kubectl scale deployment bankapp -n bankapp --replicas=1` | Disposable cloud drift test; attribute HPA vs ArgoCD corrections separately. |
| `kubectl set image deployment/bankapp bankapp=nginx:latest -n bankapp` | Disruptive disposable-lab image drift experiment; verify reconciliation restores Git. |
| `kubectl delete service bankapp-service -n bankapp` | Destructive disposable service-drift experiment; verify ArgoCD recreates it. |
| `argocd app set root-app --sync-policy none; argocd app delete root-app; argocd app delete bankapp --cascade; argocd app delete monitoring --cascade; argocd app delete envoy-gateway --cascade` | Destructive lab teardown after inspecting managed resources/data. |
| `terraform -chdir=../day-81/terraform destroy` | Destroy reviewed AWS state after Kubernetes-created load balancers and PVCs are released. |
