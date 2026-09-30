# Day 62 - Providers, resources and dependencies

## Execution status

The source files are prepared. Local validation is recorded in [validation.md](validation.md). Terraform 1.13.5, AWS CLI 2.37.6 and Ansible Core 2.21.4 were installed in the Ubuntu WSL user's local directories. The STS identity check failed with "Unable to locate credentials". No AWS resources have been created, changed or destroyed in this session.

The user selected local preparation only. The cloud exercise is **pending**, not completed. No successful apply, AWS resource IDs, lock errors, SSH results or remote idempotency evidence are claimed. Text captures are used for local evidence; no screenshots were generated. Local preparation is committed separately for this day. Cloud exercise completion and push remain pending.

## Source and dependencies

The full annotated configuration is in [terraform-aws-infra/main.tf](terraform-aws-infra/main.tf). The network includes VPC 10.0.0.0/16, public subnet 10.0.1.0/24, internet gateway, default route and subnet association. The security group allows the exercise's public TCP 22 and 80 rules and all outbound traffic. The instance uses a regional Amazon Linux 2 lookup and a public IP. No SSH key is attached in this day; a public address alone does not establish authenticated SSH reachability.

Implicit graph edges:

| Consumer | Depends on |
| --- | --- |
| Subnet, internet gateway, route table, security group | VPC |
| Route table default route | Internet gateway |
| Route table association | Subnet and route table |
| Instance | Subnet, security group and AMI data |
| Logs bucket | Instance through explicit depends_on |

The instance also explicitly waits for the route association so the network path is ready. Without a VPC, AWS cannot create its subnet. Terraform infers dependencies from attribute references and schedules prerequisites first. Destruction proceeds in reverse graph order. The DOT graph from terraform graph can be kept as text without creating an image.

## Provider versions

The AWS constraint "~> 5.0" means at least 5.0.0 and below 6.0.0. ">= 5.0" permits later major versions; "= 5.0.0" permits only that version. Check the generated .terraform.lock.hcl and validation log for the actual selection. The lock file records provider versions and package checksums; it does not lock registry module versions.

## Explicit dependencies and lifecycle

The bucket's dependency on EC2 is deliberately artificial for the exercise. In real projects an explicit dependency can ensure an IAM role policy exists before a service starts, or ensure routing is available before a bootstrap action uses the internet. Prefer direct references when the dependency is already visible.

create_before_destroy changes replacement order, potentially doubling temporary capacity and cost. prevent_destroy rejects planned destruction while the lifecycle block remains in configuration. ignore_changes delegates selected attribute updates to another manager, but may hide drift. The final instance has create_before_destroy; choose another valid regional AMI to demonstrate replacement.

## Pending AWS evidence

The five network resources, security group, instance and logs bucket are defined. Resource creation, replacement order and reverse-order cleanup have not been observed in AWS.
