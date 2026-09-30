# Day 63 Tasks

Run in Bash/Ubuntu WSL from 2026/day-63/. Cloud commands are intended steps, not evidence of execution. AWS credentials are absent. Resource creation needs cloud authorization, and deletion/state surgery needs cleanup or data-change authorization. Do not paste credentials into files or command output.

| Command | What it does |
| --- | --- |
| `export PATH="$HOME/.local/bin:$PATH"` | Expose the tools installed in the user-local bin directory. |
| `terraform version; aws --version; aws sts get-caller-identity` | Verify tools and identity before cloud execution; keep identity output private. |
| `cd terraform-variables` | Enter this day's independent Terraform project. |
| `terraform fmt -recursive; terraform init -backend=false -input=false; terraform validate` | Format and validate locally; -backend=false skips remote backend initialization and -input=false avoids prompts. |
| `terraform init` | Initialize the normal local backend before plan/apply. For shared state, configure a dedicated remote backend first. |
| `terraform plan` | Use the automatically loaded dev terraform.tfvars. |
| `terraform plan -var-file=prod.tfvars` | Override dev file values with the explicit production file. |
| `terraform plan -var="instance_type=t2.nano"` | Demonstrate the CLI sizing override with conditional sizing disabled. |
| `TF_VAR_environment=staging terraform plan` | Demonstrate that dev in terraform.tfvars outranks the environment variable. |
| `terraform apply; terraform output; terraform output instance_public_ip; terraform output -json` | After cloud authorization, apply and inspect all/single/JSON outputs. JSON outputs can reveal sensitive values. |
| `terraform console` | Enter the expression REPL; evaluate each expression in the following table, then exit. |
| `terraform plan -var-file=prod.tfvars -var="use_environment_sizing=true"; terraform apply -var-file=prod.tfvars -var="use_environment_sizing=true"` | Enable the prod/non-prod conditional sizing exercise; changes real cloud infrastructure only after authorization. |
| `terraform destroy -var-file=prod.tfvars -var="use_environment_sizing=true"` | Delete using the same environment inputs after authorization; use dev inputs instead if only dev was applied. |

## Console expressions

These are Terraform REPL inputs, not Bash commands. Evaluate separately; type exit to leave.

| Command | What it does |
| --- | --- |
| `upper("terraweek")` | Uppercase the string. |
| `join("-", ["terra", "week", "2026"])` | Join strings with a separator. |
| `format("arn:aws:s3:::%s", "my-bucket")` | Format a bucket ARN. |
| `length(["a", "b", "c"])` | Count collection entries. |
| `lookup({dev = "t2.micro", prod = "t3.small"}, "dev")` | Read the dev instance type. |
| `toset(["a", "b", "a"])` | Remove duplicate values. |
| `cidrsubnet("10.0.0.0/16", 8, 1)` | Derive subnet 10.0.1.0/24. |
| `var.environment` | Inspect tfvars versus TF_VAR precedence. |
| `var.instance_type` | Inspect CLI override behavior. |

## Submission (pending)

After completing the cloud exercises and reviewing the day evidence, run from the repository root. Do not include unrelated AGENTS.md or local caches/state. The commands below describe the later cloud completion submission. Local preparation is committed separately for this day; push was not performed.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-63/` | Stage only Day 63 after checking ignored/secret files. |
| `git commit -m "Day 63 - Completed - Complete validated infrastructure exercise"` | Create the required English completion commit only when the exercise is actually complete. |
| `git push origin master` | Publish to the configured fork branch; requires working GitHub authentication. |
