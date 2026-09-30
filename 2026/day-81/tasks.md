# Day 81 Tasks

Run from this day's directory in WSL Bash. Commands with placeholders require replacement. Cloud steps are pending where credentials are unavailable. Cleanup deletes disposable resources/data and must target only the reviewed lab.

| Command | What it does |
| --- | --- |
| `terraform version; aws --version; kubectl version --client; helm version` | Check installed tool versions; source requires Terraform >=1.5.7. |
| `mkdir -p .runtime` | Create ignored local storage. |
| `git clone --depth 1 -b feat/gitops https://github.com/TrainWithShubham/AI-BankApp-DevOps.git .runtime/AI-BankApp-DevOps` | First run only: obtain reference code on the required branch. |
| `terraform -chdir=terraform fmt -check` | Verify Terraform formatting. |
| `terraform -chdir=terraform init -backend=false -input=false` | Download providers/modules and validate locally without a state backend; no AWS creation. |
| `terraform -chdir=terraform validate -no-color` | Validate the actual configuration and installed modules. |
| `aws configure` | Interactive credential setup; keep values private. Use an existing approved profile if already configured. |
| `aws sts get-caller-identity` | Verify account identity before cloud operations; do not commit account details. |
| `terraform -chdir=terraform plan` | Preview chargeable infrastructure in the authenticated account. |
| `terraform -chdir=terraform apply` | Create paid AWS infrastructure only after reviewing account, costs and the plan. |
| `aws eks update-kubeconfig --name bankapp-eks --region us-west-2 --kubeconfig .runtime/eks-kubeconfig` | Write a private, dedicated EKS kubeconfig rather than replacing the default context. |
| `export KUBECONFIG="$PWD/.runtime/eks-kubeconfig"` | Select the dedicated kubeconfig for subsequent commands. |
| `kubectl get nodes -o wide; kubectl get nodes -L topology.kubernetes.io/zone` | Verify actual Ready nodes and AZ placement. |
| `kubectl get pods,daemonsets -n kube-system; kubectl top nodes` | Check add-on health and metrics availability. |
| `kubectl get pods,svc -n argocd` | Inspect Terraform-installed ArgoCD. |
| `python3 create-bankapp-secret.py` | Create private random BankApp credentials; requires the namespace and selected EKS context. |
| `kubectl apply --dry-run=server -f .runtime/AI-BankApp-DevOps/k8s/bankapp-deployment.yml` | Validate one manifest against the API before deployment; validate the other selected files likewise. |
| `kubectl apply -f .runtime/AI-BankApp-DevOps/k8s/namespace.yml -f .runtime/AI-BankApp-DevOps/k8s/pv.yml -f .runtime/AI-BankApp-DevOps/k8s/pvc.yml -f .runtime/AI-BankApp-DevOps/k8s/configmap.yml` | Create namespace, StorageClass, claims and configuration; do not apply upstream plaintext secrets.yml. |
| `kubectl apply -f .runtime/AI-BankApp-DevOps/k8s/mysql-deployment.yml -f .runtime/AI-BankApp-DevOps/k8s/service.yml -f .runtime/AI-BankApp-DevOps/k8s/ollama-deployment.yml -f .runtime/AI-BankApp-DevOps/k8s/bankapp-deployment.yml -f .runtime/AI-BankApp-DevOps/k8s/hpa.yml` | Deploy the app stack after credentials exist. |
| `kubectl get pods,pvc,hpa -n bankapp; kubectl get pv` | Inspect readiness, EBS-backed binding and autoscaling. |
| `kubectl port-forward svc/bankapp-service -n bankapp 8080:8080` | Access the app on loopback; stop with Ctrl-C. Test login and chatbot manually. |
| `kubectl delete namespace bankapp` | Destructive lab cleanup: confirm data can be discarded; Delete-policy PVC storage may be lost. |
| `terraform -chdir=terraform destroy` | Destructive infrastructure teardown: review the exact lab state first; verify orphan load balancers/volumes afterward. |
