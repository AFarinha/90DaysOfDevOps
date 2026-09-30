# Day 65 - Reusable Terraform modules

## Execution status

The source files are prepared. Local validation is recorded in [validation.md](validation.md). Terraform 1.13.5, AWS CLI 2.37.6 and Ansible Core 2.21.4 were installed in the Ubuntu WSL user's local directories. The STS identity check failed with "Unable to locate credentials". No AWS resources have been created, changed or destroyed in this session.

The user selected local preparation only. The cloud exercise is **pending**, not completed. No successful apply, AWS resource IDs, lock errors, SSH results or remote idempotency evidence are claimed. Text captures are used for local evidence; no screenshots were generated. Local preparation is committed separately for this day. Cloud exercise completion and push remain pending.

## Module structure

The root project [terraform-modules/](terraform-modules/) contains main.tf, variables.tf, outputs.tf, providers.tf and data.tf. Each child under modules/ec2-instance/ and modules/security-group/ contains main.tf, variables.tf, outputs.tf, providers.tf and README.md.

A root module is the configuration Terraform runs in the working directory. A child module packages resources behind inputs and outputs. Providers are configured at the root and inherited; child modules declare their provider requirement.

## Custom modules

The EC2 module takes ami_id, instance_type, subnet_id, security_group_ids, instance_name and tags. It merges the Name tag and exports instance_id, public_ip and private_ip. The security-group module takes vpc_id, sg_name, ingress_ports and tags. A dynamic ingress block produces one TCP rule per distinct port, and sg_id lets the EC2 calls reference the group.

The final root calls web_server and api_server with the same source, subnet and security group but different names. Direct file links:

- [EC2 inputs](terraform-modules/modules/ec2-instance/variables.tf), [resource](terraform-modules/modules/ec2-instance/main.tf), [outputs](terraform-modules/modules/ec2-instance/outputs.tf).
- [Root calls](terraform-modules/main.tf).

## Registry VPC and comparison

The final VPC uses terraform-aws-modules/vpc/aws pinned to 5.21.0. It has two public and two private subnets in two available zones, DNS hostnames, and no NAT gateway. Private subnets therefore have no NAT path to the internet. Registry modules are downloaded under .terraform/modules; provider versions are recorded separately in the lock file.

The hand-written Day 62 network uses five resources for one public subnet. This registry configuration covers four subnets, separate route associations and other module-managed defaults. The exact expanded resource count must be read from a real plan/apply; it is not claimed here. To practice the intermediate hand-written stage, call the child modules using a direct VPC/subnet first, then replace those inputs with module.vpc.vpc_id and module.vpc.public_subnets[0]. Do not apply that replacement to an existing deployment without reviewing replacements.

## Five practices

1. Pin module versions separately from provider versions.
2. Keep each child focused on one responsibility.
3. Accept caller inputs instead of embedding environment details.
4. Expose the IDs callers need through outputs.
5. Document inputs, outputs and lifecycle assumptions beside each module.

Local initialization checks the published module and its provider compatibility. Two running instances, real state prefixes and cleanup remain pending AWS credentials.
