# Day 70 Tasks

Run in Bash/WSL from 2026/day-70/. The tracked inventory uses reserved example addresses. Remote mutation commands require provisioned, authorized disposable Ubuntu servers. Local inventory aliases all refer to the same WSL host; only read-only or explicitly temporary-file checks were executed locally. Never run system package/user/service tasks against that local inventory.


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
| `for playbook in variables-demo.yml facts-demo.yml conditional-demo.yml loops-demo.yml server-report.yml playbooks/site.yml; do ansible-playbook -i inventory.local.ini "$playbook" --syntax-check \|\| break; done` | Validate all YAML/playbooks before remote execution. |
| `ansible-playbook -i inventory.local.ini variables-demo.yml` | Create the app directory and install the variable-defined package set. |
| `ansible-playbook -i inventory.local.ini variables-demo.yml -e "app_name=my-custom-app app_port=9090"` | Override play vars through highest-priority extra vars. |
| `ansible-playbook -i inventory.local.ini playbooks/site.yml` | Load inventory-relative group_vars and host_vars, install common packages and print web configuration. |
| `ansible web-server -i inventory.local.ini -m setup` | Collect all facts from the web host. |
| `ansible web-server -i inventory.local.ini -m setup -a "filter=ansible_os_family"; ansible web-server -i inventory.local.ini -m setup -a "filter=ansible_distribution*"` | Filter OS family and distribution facts. |
| `ansible web-server -i inventory.local.ini -m setup -a "filter=ansible_memtotal_mb"; ansible web-server -i inventory.local.ini -m setup -a "filter=ansible_default_ipv4"` | Filter memory and primary IPv4 facts. |
| `ansible-playbook -i inventory.local.ini facts-demo.yml` | Print useful facts with a fallback for missing primary network facts. |
| `ansible-playbook -i inventory.local.ini conditional-demo.yml` | Apply packages only to matching groups/OS and inspect skipped debug tasks. |
| `ansible-playbook -i inventory.local.ini loops-demo.yml` | Create users, directories and utility packages using loops; modifies disposable nodes. |
| `ansible-playbook -i inventory.local.ini server-report.yml` | Read health data and write /tmp/server-report-<host>.txt on each real node. |
| `ansible all -i inventory.local.ini -m shell -a "cat /tmp/server-report-*.txt"` | Read the generated reports; shell is required for wildcard expansion. |
| `ansible-playbook -i inventory-local.ini variables-demo.yml --tags inspect -e ansible_become=false -e "app_name=my-custom-app app_port=9090"` | Executed local alternative: print resolved variables without package or directory tasks. |
| `ansible-playbook -i inventory-local.ini playbooks/site.yml --tags inspect -e ansible_become=false` | Executed local inspection: host_vars sets max_connections to 2000. |
| `ansible-playbook -i inventory-local.ini playbooks/site.yml --tags inspect -e ansible_become=false -e max_connections=3000` | Executed local inspection: extra vars overrides host_vars. |
| `ansible-playbook -i inventory-local.ini conditional-demo.yml --tags inspect -e ansible_become=false` | Executed local OS/group condition inspection without package tasks. |
| `ansible-playbook -i inventory-local.ini loops-demo.yml --tags inspect -e ansible_become=false` | Executed local debug loop over three user specifications without creating users. |
| `ansible all -i inventory.local.ini -m file -a "path=/tmp/server-report-{{ inventory_hostname }}.txt state=absent"` | Delete only generated remote report files after cleanup authorization. |
| `cd ../../day-68/terraform-lab; terraform destroy` | From this day's ansible-practice directory, destroy the three-node AWS lab after evidence and cleanup authorization. This is the lab source path, not a change to another day. |

## Submission (pending)

After completing the cloud exercises and reviewing the day evidence, run from the repository root. Do not include unrelated AGENTS.md or local caches/state. The commands below describe the later cloud completion submission. Local preparation is committed separately for this day; push was not performed.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-70/` | Stage only Day 70 after checking ignored/secret files. |
| `git commit -m "Day 70 - Completed - Complete validated infrastructure exercise"` | Create the required English completion commit only when the exercise is actually complete. |
| `git push origin master` | Publish to the configured fork branch; requires working GitHub authentication. |
