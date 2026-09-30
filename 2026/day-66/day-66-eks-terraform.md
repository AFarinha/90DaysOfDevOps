# Day 66 - EKS with Terraform

## Execution status

The source files are prepared. Local validation is recorded in [validation.md](validation.md). Terraform 1.13.5, AWS CLI 2.37.6 and Ansible Core 2.21.4 were installed in the Ubuntu WSL user's local directories. The STS identity check failed with "Unable to locate credentials". No AWS resources have been created, changed or destroyed in this session.

The user selected local preparation only. The cloud exercise is **pending**, not completed. No successful apply, AWS resource IDs, lock errors, SSH results or remote idempotency evidence are claimed. Text captures are used for local evidence; no screenshots were generated. Local preparation is committed separately for this day. Cloud exercise completion and push remain pending.

## Configuration

The [terraform-eks/](terraform-eks/) project separates providers.tf, variables.tf, outputs.tf, terraform.tfvars, vpc.tf, eks.tf and k8s/nginx-deployment.yaml. The AWS provider uses the challenge's 5.x series; Kubernetes provider uses 2.x. The VPC module is pinned to 5.21.0 and EKS module to 20.37.2.

Two public and two private subnets span two zones. A single NAT gateway serves private nodes. Public subnet tags identify load-balancer placement; private subnet tags identify internal load-balancer placement. Nodes and cluster ENIs use private subnets, while the public subnets provide the NAT and internet-facing service path.

The cluster exposes a private API endpoint and restricts public access to supplied CIDRs. The creating identity receives cluster administrator access through the module's access entry. The managed node group uses two t3.medium nodes by default, with min 1 and max 3.

## Corrections to the older example

The README uses EKS 1.31 and AL2_x86_64. EKS stopped publishing AL2 optimized AMIs on November 26, 2025. This configuration uses AL2023_x86_64_STANDARD and requires an explicit cluster_version selected from currently available regional versions. No unsupported version is silently chosen.

Supply endpoint_allowed_cidrs as the control node public IPv4 /32. The Kubernetes provider is declared for the exercise but workload deployment is performed separately with kubectl, avoiding a provider connection to a cluster that does not yet exist.

## Workload and cleanup order

The manifest defines three Nginx replicas and a LoadBalancer Service. Verify nodes Ready, rollout completion, Service hostname and an HTTP response. Use a project-local kubeconfig so a local kind context is not overwritten.

Delete the workload and wait until the AWS load balancer and dependent network interfaces are removed before terraform destroy. Then verify EKS, node instances, VPC, NAT gateway and Elastic IP removal in AWS. Only exercise-owned resources should be inspected or deleted.

## Comparison with a local cluster

kind/minikube uses local compute and is fast to create for testing. EKS provisions an AWS-managed control plane plus IAM, VPC networking and a managed node group; it needs real credentials, cloud permissions, provisioning time and paid resources. No EKS creation time, total resource count, node readiness or HTTP success has been measured in this session.

Reference: [AWS EKS AL2 deprecation and transition](https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-deprecation-faqs.html).
