# Day 67 - Multi-environment capstone

## Execution status

The source files are prepared. Local validation is recorded in [validation.md](validation.md). Terraform 1.13.5, AWS CLI 2.37.6 and Ansible Core 2.21.4 were installed in the Ubuntu WSL user's local directories. The STS identity check failed with "Unable to locate credentials". No AWS resources have been created, changed or destroyed in this session.

The user selected local preparation only. The cloud exercise is **pending**, not completed. No successful apply, AWS resource IDs, lock errors, SSH results or remote idempotency evidence are claimed. Text captures are used for local evidence; no screenshots were generated. Local preparation is committed separately for this day. Cloud exercise completion and push remain pending.

## Layout and environment isolation

The [terraweek-capstone/](terraweek-capstone/) root contains providers.tf, variables.tf, main.tf, locals.tf, outputs.tf, data.tf, three tfvars files and modules/vpc/, modules/security-group/, modules/ec2-instance/. Each child contains its resource definitions, inputs, outputs, provider requirement and README. The day-level .gitignore applies recursively.

terraform.workspace supplies the environment name. A lifecycle precondition requires the selected workspace to match the environment value in the tfvars file, reducing accidental prod settings in dev. Workspace state separation does not provide account/IAM isolation; stronger production boundaries use separate credentials, accounts or backends.

| Environment | VPC CIDR | Public subnet | EC2 type | TCP ports |
| --- | --- | --- | --- | --- |
| dev | 10.0.0.0/16 | 10.0.1.0/24 | t2.micro | 22, 80 |
| staging | 10.1.0.0/16 | 10.1.1.0/24 | t2.small | 22, 80, 443 |
| prod | 10.2.0.0/16 | 10.2.1.0/24 | t3.small | 80, 443 |

The VPC module creates five network resources. The security-group module dynamically generates ingress rules and exports sg_id. The EC2 module accepts the AMI, type, subnet, security groups and naming/tag inputs, then exports instance_id and public_ip. Both receive explicit project_name and environment inputs. Name tags follow terraweek-<environment>-server.

## Workspace state and variable files

With the local backend, default uses terraform.tfstate and named workspaces use terraform.tfstate.d/<workspace>/terraform.tfstate. With S3, named workspaces normally use <workspace_key_prefix>/<workspace>/<key>, where the default prefix is env:. Separate directories can pin independent code/provider versions; workspaces reuse the same configuration.

Contrary to the README hint, terraform.tfvars is still auto-loaded when -var-file is supplied. Explicit files override earlier values. This project uses only named environment files to make that relationship clear.

## Best practices guide

- Split configuration by responsibility while keeping resources in focused modules.
- Use protected remote state, locking and versioning for shared/cloud runs; local state here is only a validation baseline.
- Validate inputs, and review the workspace and tfvars selection before applying.
- Pin provider and registry module versions; commit provider lock files.
- Workspaces separate state, but do not substitute for security boundaries.
- Keep state, plans, credentials and caches out of Git. Sanitized example tfvars are intentionally tracked; private values belong in ignored *.local.tfvars.
- Run fmt, validate and plan before apply.
- Apply consistent project, environment, workspace and ManagedBy tags where supported.
- Use predictable resource names.
- Destroy disposable lab resources in each workspace before deleting the workspace.

The README's example ignores all tfvars and the lock file. Here the required non-secret environment files and provider lock files remain trackable for reproducibility.

## TerraWeek concepts

| Day | Concepts |
| --- | --- |
| 61 | IaC, HCL, lifecycle commands, state basics |
| 62 | Providers, resources, dependencies, lifecycle rules |
| 63 | Variables, outputs, data sources, locals, functions |
| 64 | Remote backend, locking, import, drift |
| 65 | Custom modules, registry modules, versioning |
| 66 | EKS, VPC networking, IAM and workloads |
| 67 | Workspaces, multiple environments, capstone |

Local workspace selection can be tested without cloud provisioning. Three simultaneous AWS environments, their resource outputs and destruction remain pending.
