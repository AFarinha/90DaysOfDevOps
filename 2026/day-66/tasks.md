# Day 66 Tasks

Run in Bash/Ubuntu WSL from 2026/day-66/. Cloud commands are intended steps, not evidence of execution. AWS credentials are absent. Resource creation needs cloud authorization, and deletion/state surgery needs cleanup or data-change authorization. Do not paste credentials into files or command output.

| Command | What it does |
| --- | --- |
| `export PATH="$HOME/.local/bin:$PATH"` | Expose the tools installed in the user-local bin directory. |
| `terraform version; aws --version; aws sts get-caller-identity` | Verify tools and identity before cloud execution; keep identity output private. |
| `cd terraform-eks` | Enter this day's independent Terraform project. |
| `terraform fmt -recursive; terraform init -backend=false -input=false; terraform validate` | Format and validate locally; -backend=false skips remote backend initialization and -input=false avoids prompts. |
| `terraform init` | Initialize the normal local backend before plan/apply. For shared state, configure a dedicated remote backend first. |
| `export TF_VAR_cluster_version="REPLACE_WITH_SUPPORTED_VERSION"; export TF_VAR_endpoint_allowed_cidrs='["REPLACE_WITH_PUBLIC_IPV4/32"]'` | Supply a currently supported EKS version and API allowlist; required before plan/apply. |
| `aws eks describe-cluster-versions --region ap-south-1 --include-all` | Inspect regional EKS version availability and support before choosing a version. |
| `terraform plan; terraform apply` | Review and provision EKS, nodes, IAM, NAT and VPC after cloud/cost authorization. |
| `export KUBECONFIG="$PWD/kubeconfig"; aws eks update-kubeconfig --name "$(terraform output -raw cluster_name)" --region "$(terraform output -raw cluster_region)"` | Create an ignored project-local kubeconfig; avoids overwriting the local cluster context. |
| `kubectl get nodes; kubectl get pods -A; kubectl cluster-info` | Verify two Ready managed nodes and control-plane connectivity. |
| `kubectl apply --dry-run=client -f k8s/nginx-deployment.yaml; kubectl apply --dry-run=server -f k8s/nginx-deployment.yaml` | Validate manifests locally and against EKS before applying. |
| `kubectl apply -f k8s/nginx-deployment.yaml; kubectl rollout status deployment/nginx-terraweek --timeout=300s` | Create the workload and paid load balancer, then wait for the three replicas. |
| `kubectl get svc nginx-service -w` | Observe the LoadBalancer hostname; stop watching with Ctrl+C. |
| `curl -fsS "http://$(kubectl get svc nginx-service -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')"` | Request the Nginx page once a hostname is assigned. |
| `kubectl get nodes; kubectl get deployments,pods,svc` | Record actual workload and node status. |
| `kubectl delete -f k8s/nginx-deployment.yaml` | Delete only the exercise workload and Service after cleanup authorization; wait for AWS load-balancer removal before destroy. |
| `terraform destroy` | Delete EKS and its infrastructure after the load balancer is gone; verify EKS, EC2, NAT, EIPs and VPC in AWS. |
| `unset KUBECONFIG TF_VAR_cluster_version TF_VAR_endpoint_allowed_cidrs` | Restore the shell to its default kubeconfig and clear temporary inputs. |

## Submission (pending)

After completing the cloud exercises and reviewing the day evidence, run from the repository root. Do not include unrelated AGENTS.md or local caches/state. The commands below describe the later cloud completion submission. Local preparation is committed separately for this day; push was not performed.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-66/` | Stage only Day 66 after checking ignored/secret files. |
| `git commit -m "Day 66 - Completed - Complete validated infrastructure exercise"` | Create the required English completion commit only when the exercise is actually complete. |
| `git push origin master` | Publish to the configured fork branch; requires working GitHub authentication. |
