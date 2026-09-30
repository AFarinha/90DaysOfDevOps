# Day 61 Tasks

Run in Bash/Ubuntu WSL from 2026/day-61/. Cloud commands are intended steps, not evidence of execution. AWS credentials are absent. Resource creation needs cloud authorization, and deletion/state surgery needs cleanup or data-change authorization. Do not paste credentials into files or command output.

| Command | What it does |
| --- | --- |
| `export PATH="$HOME/.local/bin:$PATH"` | Expose the tools installed in the user-local bin directory. |
| `terraform version; aws --version; aws sts get-caller-identity` | Verify tools and identity before cloud execution; keep identity output private. |
| `cd terraform-basics` | Enter this day's independent Terraform project. |
| `terraform fmt -recursive; terraform init -backend=false -input=false; terraform validate` | Format and validate locally; -backend=false skips remote backend initialization and -input=false avoids prompts. |
| `terraform init` | Initialize the normal local backend before plan/apply. For shared state, configure a dedicated remote backend first. |
| `export TF_VAR_bucket_name="REPLACE_WITH_GLOBALLY_UNIQUE_NAME"; export TF_VAR_ami_id="REPLACE_WITH_VERIFIED_REGIONAL_AMI"` | Provide required non-secret inputs after selecting the region and verifying the AMI. |
| `terraform plan -target=aws_s3_bucket.first` | Preview only the first S3 stage; targeting is an exercise aid, not the normal workflow. |
| `terraform apply -target=aws_s3_bucket.first` | Create the bucket after reviewing the targeted plan; creates AWS resources. |
| `terraform plan -var="instance_name=TerraWeek-Day1"; terraform apply -var="instance_name=TerraWeek-Day1"` | Preview and create EC2 alongside the existing bucket; requires cloud authorization. |
| `terraform show; terraform state list; terraform state show aws_s3_bucket.first; terraform state show aws_instance.main` | Inspect state and compare cloud IDs; do not publish raw state, which may contain secrets. |
| `terraform plan; terraform apply` | Use the final default TerraWeek-Modified Name tag; review the in-place update before applying. |
| `terraform destroy` | Delete only this project state resources after cleanup authorization; verify S3/EC2 removal in AWS. |

## Submission (pending)

After completing the cloud exercises and reviewing the day evidence, run from the repository root. Do not include unrelated AGENTS.md or local caches/state. The commands below describe the later cloud completion submission. Local preparation is committed separately for this day; push was not performed.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-61/` | Stage only Day 61 after checking ignored/secret files. |
| `git commit -m "Day 61 - Completed - Complete validated infrastructure exercise"` | Create the required English completion commit only when the exercise is actually complete. |
| `git push origin master` | Publish to the configured fork branch; requires working GitHub authentication. |
