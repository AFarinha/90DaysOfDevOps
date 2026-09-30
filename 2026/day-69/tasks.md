# Day 69 Tasks

Run in Bash/WSL from 2026/day-69/. The tracked inventory uses reserved example addresses. Remote mutation commands require provisioned, authorized disposable Ubuntu servers. Local inventory aliases all refer to the same WSL host; only read-only or explicitly temporary-file checks were executed locally. Never run system package/user/service tasks against that local inventory.


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
| `for playbook in install-nginx.yml essential-modules.yml nginx-config.yml multi-play.yml; do ansible-playbook -i inventory.local.ini "$playbook" --syntax-check \|\| break; done` | Check every playbook before any mutation. |
| `ansible-playbook -i inventory.local.ini install-nginx.yml --check --diff` | Preview installation and file changes; check mode can be incomplete on a fresh host. |
| `ansible-playbook -i inventory.local.ini install-nginx.yml; ansible-playbook -i inventory.local.ini install-nginx.yml` | Run twice and compare real changed/ok counts to verify idempotency on EC2. |
| `curl -fsS http://REPLACE_WITH_WEB_PUBLIC_IP` | Verify the custom web page from the allowed client IP. |
| `ansible-playbook -i inventory.local.ini essential-modules.yml` | Practice the seven essential module types on the disposable Ubuntu nodes. |
| `ansible-playbook -i inventory.local.ini essential-modules.yml --tags remove-package` | Optional package-removal exercise: removes tree; do not combine with the standard installation verification. |
| `ansible-playbook -i inventory.local.ini nginx-config.yml --check --diff` | Preview the custom Nginx config and page. |
| `ansible-playbook -i inventory.local.ini nginx-config.yml; ansible-playbook -i inventory.local.ini nginx-config.yml` | Validate/deploy configuration and compare first/second handler runs. |
| `ansible-playbook -i inventory.local.ini install-nginx.yml -v` | Verbose execution alternative; use -vv or -vvv only for additional debugging. |
| `ansible-playbook -i inventory.local.ini install-nginx.yml --limit web-server` | Limit execution to the named web host. |
| `ansible-playbook -i inventory.local.ini multi-play.yml --list-hosts --list-tasks` | Check separate group targeting without executing tasks. |
| `ansible-playbook -i inventory.local.ini multi-play.yml` | Apply distinct web/app/db configuration. |
| `ansible-playbook -i inventory-local.ini essential-modules.yml --tags diagnostics -e ansible_become=false` | Executed local alternative: read disk/process output only, with privilege escalation disabled during fact gathering. |
| `ansible-playbook -i inventory-local.ini multi-play.yml --list-hosts --list-tasks` | Executed local alternative: inspect scope, with no package/service changes. |

## Submission (pending)

After completing the cloud exercises and reviewing the day evidence, run from the repository root. Do not include unrelated AGENTS.md or local caches/state. The commands below describe the later cloud completion submission. Local preparation is committed separately for this day; push was not performed.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-69/` | Stage only Day 69 after checking ignored/secret files. |
| `git commit -m "Day 69 - Completed - Complete validated infrastructure exercise"` | Create the required English completion commit only when the exercise is actually complete. |
| `git push origin master` | Publish to the configured fork branch; requires working GitHub authentication. |
