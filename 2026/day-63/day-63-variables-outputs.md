# Day 63 - Variables, outputs, data sources and expressions

## Execution status

The source files are prepared. Local validation is recorded in [validation.md](validation.md). Terraform 1.13.5, AWS CLI 2.37.6 and Ansible Core 2.21.4 were installed in the Ubuntu WSL user's local directories. The STS identity check failed with "Unable to locate credentials". No AWS resources have been created, changed or destroyed in this session.

The user selected local preparation only. The cloud exercise is **pending**, not completed. No successful apply, AWS resource IDs, lock errors, SSH results or remote idempotency evidence are claimed. Text captures are used for local evidence; no screenshots were generated. Local preparation is committed separately for this day. Cloud exercise completion and push remain pending.

## Files and types

The [terraform-variables/](terraform-variables/) directory contains variables.tf, main.tf, data.tf, locals.tf, outputs.tf, providers.tf, terraform.tfvars and prod.tfvars. The required project_name has no default; the dev tfvars supplies it. Primitive types string, number and bool describe scalar values; list(number) and map(string) constrain collections. use_environment_sizing provides a bool example.

| Input | Dev | Prod |
| --- | --- | --- |
| project_name | terraweek | terraweek |
| environment | dev | prod |
| instance_type | t2.micro | t3.small |
| vpc_cidr | 10.0.0.0/16 | 10.1.0.0/16 |
| subnet_cidr | 10.0.1.0/24 | 10.1.1.0/24 |

## Correct CLI variable precedence

Lowest to highest: default, TF_VAR environment variables, terraform.tfvars, terraform.tfvars.json, *.auto.tfvars / *.auto.tfvars.json in lexical order, then -var and -var-file options in the order supplied.

The README hint incorrectly puts TF_VAR last. TF_VAR_environment=staging does not override environment=dev in terraform.tfvars. prod.tfvars overrides the dev values when explicitly supplied. A later -var can override a preceding -var-file.

The default sizing uses var.instance_type so a CLI override is effective. Enable use_environment_sizing=true to practice the requested conditional: prod selects t3.small; other environments select t2.micro. With this option enabled the conditional intentionally overrides instance_type.

## Values and outputs

A variable is a caller-supplied input; a local computes reusable expressions; an output exposes results; a data source reads external information without creating it. The AMI data source restricts owner to Amazon and matches AL2 x86_64 HVM EBS gp2 image names. gp2 is part of the image name, not a valid root-device-type filter value. Availability zones come from AWS; the first available zone is used.

Common tags merge caller tags with enforced project, environment and ManagedBy values. Resource-specific Name tags use the project/environment prefix. Six outputs expose VPC, subnet, instance, public IP, public DNS and security group IDs. Actual values require a successful apply.

## Useful functions

| Function | Use |
| --- | --- |
| format | Build predictable names and ARN strings. |
| merge | Combine tag maps; later map values win. |
| cidrsubnet | Derive subnet CIDRs from a larger network. |
| lookup | Read a map value with an optional fallback. |
| toset | Deduplicate values for dynamic rules. |

The console exercises also cover upper, join and length. Their real local results and variable precedence checks belong in validation.md. Cloud outputs and instance type changes are pending.

Reference: [HashiCorp input variable precedence](https://developer.hashicorp.com/terraform/language/values/variables).
