# Day 62 Tasks

Run in Bash/Ubuntu WSL from 2026/day-62/. Cloud commands are intended steps, not evidence of execution. AWS credentials are absent. Resource creation needs cloud authorization, and deletion/state surgery needs cleanup or data-change authorization. Do not paste credentials into files or command output.

| Command | What it does |
| --- | --- |
| `export PATH="$HOME/.local/bin:$PATH"` | Expose the tools installed in the user-local bin directory. |
| `terraform version; aws --version; aws sts get-caller-identity` | Verify tools and identity before cloud execution; keep identity output private. |
| `cd terraform-aws-infra` | Enter this day's independent Terraform project. |
| `terraform fmt -recursive; terraform init -backend=false -input=false; terraform validate` | Format and validate locally; -backend=false skips remote backend initialization and -input=false avoids prompts. |
| `terraform init` | Initialize the normal local backend before plan/apply. For shared state, configure a dedicated remote backend first. |
| `terraform plan -target=aws_vpc.main -target=aws_subnet.public -target=aws_internet_gateway.main -target=aws_route_table.public -target=aws_route_table_association.public` | Preview the five network resources for the initial task; follow with a full plan. |
| `terraform apply -target=aws_vpc.main -target=aws_subnet.public -target=aws_internet_gateway.main -target=aws_route_table.public -target=aws_route_table_association.public` | Create the initial network stage after authorization. |
| `terraform plan; terraform apply` | Review and deploy the full security group, EC2 and dependency-controlled logs bucket; public SSH is a lab-only rule. |
| `terraform graph > graph.dot` | Save the actual DOT dependency graph as text; no screenshot is required. |
| `terraform plan -replace=aws_instance.main` | Preview replacement and create-before-destroy order; do not apply blindly. For the AMI task, edit the regional AMI filter to choose another verified image first. |
| `terraform destroy` | Delete the exercise stack in reverse dependency order after cleanup authorization. |

## Submission (pending)

After completing the cloud exercises and reviewing the day evidence, run from the repository root. Do not include unrelated AGENTS.md or local caches/state. The commands below describe the later cloud completion submission. Local preparation is committed separately for this day; push was not performed.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-62/` | Stage only Day 62 after checking ignored/secret files. |
| `git commit -m "Day 62 - Completed - Complete validated infrastructure exercise"` | Create the required English completion commit only when the exercise is actually complete. |
| `git push origin master` | Publish to the configured fork branch; requires working GitHub authentication. |
