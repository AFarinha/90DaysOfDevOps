# Day 64 Tasks

Run in Bash/Ubuntu WSL from 2026/day-64/. Cloud commands are intended steps, not evidence of execution. AWS credentials are absent. Resource creation needs cloud authorization, and deletion/state surgery needs cleanup or data-change authorization. Do not paste credentials into files or command output.

| Command | What it does |
| --- | --- |
| `export PATH="$HOME/.local/bin:$PATH"` | Expose the tools installed in the user-local bin directory. |
| `terraform version; aws --version; aws sts get-caller-identity` | Verify tools and identity before cloud execution; keep identity output private. |
| `cd terraform-state` | Enter this day's independent Terraform project. |
| `terraform fmt -recursive; terraform init -backend=false -input=false; terraform validate` | Format and validate locally; -backend=false skips remote backend initialization and -input=false avoids prompts. |
| `terraform plan; terraform apply` | Create the baseline local-state project only after cloud authorization. |
| `terraform show; terraform state list; terraform state show aws_instance.main; terraform state show aws_vpc.main` | Inspect applied state without copying secrets to documentation. |
| `export STATE_BUCKET="REPLACE_WITH_UNIQUE_NAME"; export IMPORT_BUCKET="REPLACE_WITH_UNIQUE_IMPORT_NAME"; export AWS_REGION=ap-south-1` | Set non-secret backend/import names and the selected region. |
| `aws s3api create-bucket --bucket "$STATE_BUCKET" --region "$AWS_REGION" --create-bucket-configuration LocationConstraint="$AWS_REGION"` | Create the dedicated backend bucket after authorization; us-east-1 requires omitting LocationConstraint. |
| `aws s3api put-bucket-versioning --bucket "$STATE_BUCKET" --versioning-configuration Status=Enabled` | Enable state recovery versions. |
| `aws s3api put-bucket-encryption --bucket "$STATE_BUCKET" --server-side-encryption-configuration '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'` | Configure explicit server-side state encryption. |
| `aws s3api put-public-access-block --bucket "$STATE_BUCKET" --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true` | Block public access to the state bucket. |
| `aws dynamodb create-table --table-name terraweek-state-lock --attribute-definitions AttributeName=LockID,AttributeType=S --key-schema AttributeName=LockID,KeyType=HASH --billing-mode PAY_PER_REQUEST --region "$AWS_REGION"` | Create the exercise lock table; DynamoDB locking is deprecated but retained for this lesson. |
| `aws dynamodb wait table-exists --table-name terraweek-state-lock --region "$AWS_REGION"` | Wait until the lock table exists before migration. |
| `cp backend.tf.example backend.tf; cp backend.hcl.example backend.hcl` | Activate backend templates; edit backend.hcl with your bucket/region before the next command. Do not overwrite an existing backend file. |
| `terraform init -migrate-state -backend-config=backend.hcl` | Copy the existing local state to S3 after reviewing the migration prompt; do not overwrite unrelated remote state. |
| `aws s3api head-object --bucket "$STATE_BUCKET" --key dev/terraform.tfstate; terraform plan` | Verify the remote object and an unchanged plan; do not output the object contents. |
| `terraform apply` | Terminal A: leave a genuine pending change at confirmation to hold the lock. Cancel after the lock test. |
| `terraform plan -lock-timeout=5s` | Terminal B: test contention while A holds the lock; record the actual error. |
| `terraform force-unlock LOCK_ID` | Recovery alternative only: releases a verified stale lock after confirming no active owner; requires authorization. |
| `aws s3api create-bucket --bucket "$IMPORT_BUCKET" --region "$AWS_REGION" --create-bucket-configuration LocationConstraint="$AWS_REGION"` | Create a bucket outside Terraform for the import exercise. |
| `cp import.tf.example import.tf` | Activate the import definition; edit its bucket name before importing. |
| `terraform import aws_s3_bucket.imported "$IMPORT_BUCKET"; terraform plan` | Attach the existing bucket to state and compare its config without creating it. |
| `terraform state mv aws_s3_bucket.imported aws_s3_bucket.logs_bucket` | Rename state address after renaming the matching resource block; state mutation requires authorization. |
| `terraform state rm aws_s3_bucket.logs_bucket` | Forget the bucket without deleting it. Do not apply before re-import; requires authorization. |
| `terraform import aws_s3_bucket.logs_bucket "$IMPORT_BUCKET"; terraform plan` | Restore management and verify alignment. |
| `aws ec2 create-tags --resources "$(terraform output -raw instance_id)" --tags Key=Name,Value=ManuallyChanged` | Make a deliberate exercise-owned tag drift after authorization. |
| `terraform plan; terraform apply; terraform plan` | Detect and reconcile the drift, then verify no further changes. |
| `terraform plan -refresh-only` | Optional alternative preview: state-only refresh does not reconcile infrastructure. |
| `terraform destroy` | Delete managed lab resources, including the re-imported bucket, after cleanup authorization; retain the backend. |
| `aws s3api list-object-versions --bucket "$STATE_BUCKET"` | Review the exercise state versions before any backend cleanup. Backend deletion must wait until no configuration uses it. |
| `aws dynamodb delete-table --table-name terraweek-state-lock --region "$AWS_REGION"` | Optional backend cleanup after all users/states are retired; destructive and requires authorization. |
| `aws s3api delete-bucket --bucket "$STATE_BUCKET"` | Optional final backend cleanup after authorized deletion of every object version/delete marker; fails while version history remains. Never use broad deletion against a shared bucket. |

## Submission (pending)

After completing the cloud exercises and reviewing the day evidence, run from the repository root. Do not include unrelated AGENTS.md or local caches/state. The commands below describe the later cloud completion submission. Local preparation is committed separately for this day; push was not performed.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-64/` | Stage only Day 64 after checking ignored/secret files. |
| `git commit -m "Day 64 - Completed - Complete validated infrastructure exercise"` | Create the required English completion commit only when the exercise is actually complete. |
| `git push origin master` | Publish to the configured fork branch; requires working GitHub authentication. |
