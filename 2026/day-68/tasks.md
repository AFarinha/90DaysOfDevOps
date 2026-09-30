# Day 68 Tasks

Run in Bash/WSL from 2026/day-68/. The tracked inventory uses reserved example addresses. Remote mutation commands require provisioned, authorized disposable Ubuntu servers. Local inventory aliases all refer to the same WSL host; only read-only or explicitly temporary-file checks were executed locally. Never run system package/user/service tasks against that local inventory.

## AWS lab setup

Use an existing EC2 key pair matching an external private key. Keep the three instances for days 69-70 and destroy them afterward. These cloud steps have not run.

| Command | What it does |
| --- | --- |
| `cd terraform-lab; terraform fmt -recursive; terraform init; terraform validate` | Initialize and validate the three-node lab. |
| `export TF_VAR_key_name="REPLACE_WITH_EXISTING_KEY_PAIR"; export TF_VAR_ssh_cidr="REPLACE_WITH_CONTROL_PUBLIC_IPV4/32"` | Set required non-secret SSH inputs; do not put private key data in HCL. |
| `terraform plan; terraform apply` | Review and create the three paid EC2 instances and network only after cloud authorization. |
| `terraform output -json server_ips` | Read web/app/db IPs for the ignored inventory. |
| `cd ..` | Return to the day directory before entering ansible-practice. |
| `ssh -i ~/.ssh/terraweek.pem ubuntu@REPLACE_WITH_SERVER_IP` | Repeat for each server and verify the host fingerprint through a trusted channel. |
| `cd ../terraform-lab; terraform destroy` | From ansible-practice, remove the exercise lab after days 69-70 and cleanup authorization; retain unrelated AWS resources. |

## Ansible commands

| Command | What it does |
| --- | --- |
| `export PATH="$HOME/.local/bin:$PATH"` | Use the installed user-local tools. |
| `ansible --version` | Verify the control-node Ansible and Python versions. |
| `cd ansible-practice` | Enter the inventory/playbook directory. Relative paths in the tables are from here. |
| `ansible-inventory -i inventory.ini --graph` | Check parsed groups without connecting to placeholder hosts. |
| `cp inventory.ini inventory.local.ini` | Create an ignored remote inventory; replace reserved IPs with real EC2 outputs and verify the key path. Do not overwrite an existing inventory. |
| `ansible all -i inventory.local.ini -m ping` | Verify Python/SSH execution on real managed nodes; not an ICMP ping. |
| `ansible all -i inventory-local.ini -m ping` | Local alternative: all aliases refer to one WSL machine, not EC2. |
| `ansible all -i inventory.local.ini -m command -a "uptime"` | Read uptime from all real nodes. |
| `ansible web -i inventory.local.ini -m command -a "free -h"` | Read human-readable memory from web. |
| `ansible all -i inventory.local.ini -m command -a "df -h"` | Read filesystem usage. |
| `ansible web -i inventory.local.ini -m apt -a "name=git state=present update_cache=true" --become` | Install Git on Ubuntu web nodes; modifies system packages. Use -K if sudo needs a password. |
| `ansible all -i inventory.local.ini -m copy -a "src=hello.txt dest=/tmp/day68-hello.txt mode=0644"` | Copy the sample file to each remote node. |
| `ansible all -i inventory.local.ini -m command -a "cat /tmp/day68-hello.txt"` | Read the copied sample. |
| `ansible application -i inventory.local.ini -m ping; ansible db -i inventory.local.ini -m ping; ansible all_servers -i inventory.local.ini -m ping` | Exercise group-of-groups and database selection. |
| `ansible "web:app" -i inventory.local.ini -m ping; ansible "all:!db" -i inventory.local.ini -m ping` | Exercise OR and exclusion patterns; quote special characters. |
| `ANSIBLE_INVENTORY=inventory.local.ini ansible all -m ping` | Use the real inventory without a -i flag; the tracked default remains the placeholder inventory. |
| `ansible all -i inventory.local.ini -m file -a "path=/tmp/day68-hello.txt state=absent"` | Cleanup only the exercise copy after authorization; deletes that file on each target. |

## Submission (pending)

After completing the cloud exercises and reviewing the day evidence, run from the repository root. Do not include unrelated AGENTS.md or local caches/state. The commands below describe the later cloud completion submission. Local preparation is committed separately for this day; push was not performed.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-68/` | Stage only Day 68 after checking ignored/secret files. |
| `git commit -m "Day 68 - Completed - Complete validated infrastructure exercise"` | Create the required English completion commit only when the exercise is actually complete. |
| `git push origin master` | Publish to the configured fork branch; requires working GitHub authentication. |
