# Day 67 Tasks

Run in Bash/Ubuntu WSL from 2026/day-67/. Cloud commands are intended steps, not evidence of execution. AWS credentials are absent. Resource creation needs cloud authorization, and deletion/state surgery needs cleanup or data-change authorization. Do not paste credentials into files or command output.

| Command | What it does |
| --- | --- |
| `export PATH="$HOME/.local/bin:$PATH"` | Expose the tools installed in the user-local bin directory. |
| `terraform version; aws --version; aws sts get-caller-identity` | Verify tools and identity before cloud execution; keep identity output private. |
| `cd terraweek-capstone` | Enter this day's independent Terraform project. |
| `terraform fmt -recursive; terraform init -backend=false -input=false; terraform validate` | Format and validate locally; -backend=false skips remote backend initialization and -input=false avoids prompts. |
| `terraform init` | Initialize the normal local backend before plan/apply. For shared state, configure a dedicated remote backend first. |
| `terraform workspace show; terraform workspace list` | Inspect the current workspace before choosing environment inputs. |
| `terraform workspace new dev` | Create the dev workspace once; use select instead when it already exists. |
| `terraform workspace select dev; terraform plan -var-file=dev.tfvars; terraform apply -var-file=dev.tfvars` | Deploy dev after reviewing the plan and cloud authorization. The guard rejects mismatched environment/workspace inputs. |
| `terraform output` | Capture real outputs while the corresponding workspace is selected. |
| `terraform workspace new staging` | Create the staging workspace once; use select instead when it already exists. |
| `terraform workspace select staging; terraform plan -var-file=staging.tfvars; terraform apply -var-file=staging.tfvars` | Deploy staging after reviewing the plan and cloud authorization. The guard rejects mismatched environment/workspace inputs. |
| `terraform output` | Capture real outputs while the corresponding workspace is selected. |
| `terraform workspace new prod` | Create the prod workspace once; use select instead when it already exists. |
| `terraform workspace select prod; terraform plan -var-file=prod.tfvars; terraform apply -var-file=prod.tfvars` | Deploy prod after reviewing the plan and cloud authorization. The guard rejects mismatched environment/workspace inputs. |
| `terraform output` | Capture real outputs while the corresponding workspace is selected. |
| `terraform workspace select prod; terraform destroy -var-file=prod.tfvars` | Delete prod resources after cleanup authorization; use matching inputs. |
| `terraform workspace select staging; terraform destroy -var-file=staging.tfvars` | Delete staging resources after cleanup authorization; use matching inputs. |
| `terraform workspace select dev; terraform destroy -var-file=dev.tfvars` | Delete dev resources after cleanup authorization; use matching inputs. |
| `terraform workspace select default` | Switch away from named workspaces before deletion. |
| `terraform workspace delete dev; terraform workspace delete staging; terraform workspace delete prod` | Delete only empty exercise workspace metadata after resource destruction; do not use -force. |

## Submission (pending)

After completing the cloud exercises and reviewing the day evidence, run from the repository root. Do not include unrelated AGENTS.md or local caches/state. The commands below describe the later cloud completion submission. Local preparation is committed separately for this day; push was not performed.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-67/` | Stage only Day 67 after checking ignored/secret files. |
| `git commit -m "Day 67 - Completed - Complete validated infrastructure exercise"` | Create the required English completion commit only when the exercise is actually complete. |
| `git push origin master` | Publish to the configured fork branch; requires working GitHub authentication. |
