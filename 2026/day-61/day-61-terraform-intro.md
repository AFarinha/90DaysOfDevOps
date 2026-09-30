# Day 61 - Terraform introduction

## Execution status

The source files are prepared. Local validation is recorded in [validation.md](validation.md). Terraform 1.13.5, AWS CLI 2.37.6 and Ansible Core 2.21.4 were installed in the Ubuntu WSL user's local directories. The STS identity check failed with "Unable to locate credentials". No AWS resources have been created, changed or destroyed in this session.

The user selected local preparation only. The cloud exercise is **pending**, not completed. No successful apply, AWS resource IDs, lock errors, SSH results or remote idempotency evidence are claimed. Text captures are used for local evidence; no screenshots were generated. Local preparation is committed separately for this day. Cloud exercise completion and push remain pending.

## Infrastructure as Code

IaC describes infrastructure in files that can be reviewed, versioned and applied consistently. It replaces undocumented console clicks with a reproducible description of the desired resources. Terraform compares this description, its state and the provider's view of the cloud to propose changes. A reviewed plan helps catch unwanted replacements before provisioning.

Terraform is declarative: the configuration says what should exist; its dependency graph decides the execution order. Providers let it manage multiple platforms, although AWS resource definitions are not portable unchanged to another cloud. CloudFormation is AWS-native; Ansible mainly configures existing machines; Pulumi describes infrastructure using general-purpose programming languages.

## Configuration and exercise order

The project is in [terraform-basics/](terraform-basics/), with main.tf, providers.tf and variables.tf. Supply a globally unique bucket name and an AMI verified for the selected region. The final default Name tag is TerraWeek-Modified. Start with the S3-only target, then add EC2 with the full apply, then change the tag. Targeting is used only to reproduce the staged introductory exercise; full plans are required afterward.

No AMI ID is invented. The intended instance type is t2.micro; account eligibility and actual pricing must be checked before deployment. This initial exercise assumes a default VPC with an available subnet in the chosen region.

## Lifecycle and state

| Command | Purpose |
| --- | --- |
| terraform init | Initialize the working directory, backend and provider dependencies. |
| terraform plan | Refresh/read resource information and preview differences. |
| terraform apply | Apply the reviewed changes and update state. |
| terraform destroy | Remove resources tracked in the selected state. |
| terraform show | Show state, or a saved plan when given a plan path. |
| terraform state list | List managed resource addresses. |
| terraform state show | Inspect one resource's recorded attributes. |

The .terraform directory holds initialized backend metadata, provider plugins and downloaded modules. The dependency lock file records provider selections and checksums and should be tracked. State maps Terraform addresses to remote IDs and stores attributes, dependencies, outputs, lineage and serial. Terraform uses that mapping to recognize an existing bucket and avoid recreating it when EC2 is added.

Do not edit state by hand: broken mappings can cause duplicate resources or unintended changes. State can contain secrets and belongs in a protected backend, not Git. A tag update normally uses an in-place "~" change; "+" means create and "-" means destroy. A replacement shows both create and destroy markers. These are explanations, not captured AWS plan results.

## Remaining evidence

S3 creation, EC2 creation, state inspection, tag modification and final destroy verification still require AWS credentials and a real apply.
