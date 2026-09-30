# Day 64 - State management and remote backends

## Execution status

The source files are prepared. Local validation is recorded in [validation.md](validation.md). Terraform 1.13.5, AWS CLI 2.37.6 and Ansible Core 2.21.4 were installed in the Ubuntu WSL user's local directories. The STS identity check failed with "Unable to locate credentials". No AWS resources have been created, changed or destroyed in this session.

The user selected local preparation only. The cloud exercise is **pending**, not completed. No successful apply, AWS resource IDs, lock errors, SSH results or remote idempotency evidence are claimed. Text captures are used for local evidence; no screenshots were generated. Local preparation is committed separately for this day. Cloud exercise completion and push remain pending.

## Project and backend transition

The [terraform-state/](terraform-state/) project is independently runnable and starts with local state. backend.tf.example and backend.hcl.example are inactive templates so local init/validate can run without a configured bucket. After creating the dedicated state bucket and DynamoDB lock table, activate backend.tf, create backend.hcl with real non-secret names, and run init -migrate-state. Backend credentials come from the AWS credential chain, never the HCL file.

Local flow: Terraform -> local terraform.tfstate -> AWS resources.
Remote flow: Terraform -> encrypted/versioned S3 state, with DynamoDB LockID coordination -> AWS resources.

S3 versioning provides recovery versions; encryption protects stored state; locking prevents concurrent writers. DynamoDB locking is retained to match this challenge but is deprecated in current Terraform. Modern projects can use S3 use_lockfile=true with the required object permissions. The backend bucket and lock table must outlive every configuration that uses them.

## Inspecting state

The configuration defines seven managed AWS resources before adding the imported bucket. This is a configuration count, not an observed state count. terraform state list is the authoritative way to count applied resources. An EC2 state record includes its remote ID, AMI, type, tags, IPs, DNS, subnet, security groups and computed provider attributes. serial increases when Terraform writes a changed snapshot; lineage identifies the state history.

## Import and state operations

| Operation | Meaning and precautions |
| --- | --- |
| import | Attach an existing AWS object to a configured address; it does not create the object or generate its desired configuration automatically. |
| state mv | Change an address while keeping its remote object; update configuration to the new address as well. |
| state rm | Forget the object without deleting it; if its resource block stays, the next plan proposes another object. |
| force-unlock | Release a stale lock only after verifying that its owning operation has stopped. |
| apply -refresh-only | Accept observed remote changes into state after review; it does not reconcile the cloud to the desired configuration. |
| plan / apply | Detect drift, then reconcile remote infrastructure to the configuration. |

Import the manually created bucket as aws_s3_bucket.imported. Rename the block and state address to logs_bucket together. After removing the address, immediately re-import before applying; otherwise a duplicate-name bucket create will fail. No state commands were run against AWS in this session.

## Locking and drift

For a meaningful lock test, make a real pending change in terminal A and leave apply awaiting confirmation. A no-op apply may finish immediately, so it is not a reliable contention demonstration. Terminal B can run plan -lock-timeout=5s; record the actual lock error, then cancel terminal A. Never fabricate a lock ID.

Change the EC2 Name tag outside Terraform, run plan, reconcile with apply, and verify a subsequent no-change plan. Restrict manual cloud changes and route updates through reviewed automation to reduce drift. The actual drift exercise and lock test are pending.

Reference: [HashiCorp S3 backend and locking](https://developer.hashicorp.com/terraform/language/backend/s3).
