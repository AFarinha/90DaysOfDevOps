# Day 70 - Ansible variables, facts, conditionals and loops

## Execution status

The source files are prepared. Local validation is recorded in [validation.md](validation.md). Terraform 1.13.5, AWS CLI 2.37.6 and Ansible Core 2.21.4 were installed in the Ubuntu WSL user's local directories. The STS identity check failed with "Unable to locate credentials". No AWS resources have been created, changed or destroyed in this session.

The user selected local preparation only. The cloud exercise is **pending**, not completed. No successful apply, AWS resource IDs, lock errors, SSH results or remote idempotency evidence are claimed. Text captures are used for local evidence; no screenshots were generated. Local preparation is committed separately for this day. Cloud exercise completion and push remain pending.

## Variables and file structure

The [ansible-practice/](ansible-practice/) directory contains variables-demo.yml, facts-demo.yml, conditional-demo.yml, loops-demo.yml, server-report.yml, playbooks/site.yml, inventory.ini and ansible.cfg. group_vars/all.yml contains common packages and app_env; web.yml contains http_port and max_connections=1000; db.yml contains the MySQL package list. host_vars/web-server.yml sets max_connections=2000 and its custom message.

The local inspections print the host override as 2000 and an extra-var override as 3000. variables-demo's CLI values change the debug output to my-custom-app and port 9090. Package and directory tasks were omitted from these local inspections.

Simplified precedence, low to high: role defaults -> inventory group vars -> inventory host vars -> play vars -> task vars -> extra vars. The README task's suggestion that host_vars outranks play vars is incorrect; its later hints give the correct relative order. More sources exist in the full Ansible precedence rules.

## Useful facts

| Fact | Practical use |
| --- | --- |
| os_family | Select compatible package managers and service paths. |
| distribution / distribution_version | Gate version-specific configuration. |
| memtotal_mb | Adjust application capacity or flag low-memory hosts. |
| default_ipv4.address | Report a primary address when available. |
| service_mgr | Use systemd commands only on systemd systems. |

The playbooks use ansible_facts dictionary access to avoid relying on injected top-level facts. Missing network facts are reported as unavailable, not invented.

## Conditionals and loops

conditional-demo.yml gates package tasks by web/db membership and Debian family. Debug checks demonstrate OS selection, memory thresholds, production environment, AND and OR conditions. The local inspect run shows actual skipped and executed tasks without installing packages.

loops-demo.yml iterates over user dictionaries, directories and packages. Ubuntu uses the sudo group rather than the RHEL wheel group. append=true retains existing supplemental memberships. The local run prints the three requested users; it does not create them. loop is the normal modern syntax; older with_* lookup forms are not all interchangeable one-for-one, and flattening/lookups may need explicit filters.

## Server report and corrected disk check

server-report.yml reads df -P /, free -m and systemd services where available, registers output and writes one report per inventory host. Disk use is parsed numerically and compared with >=90. The README's literal substring '9[0-9]%' does not implement a regular expression, so it would miss many full-disk cases.

The local run generated reports for the three aliases using facts from the same WSL machine. The sample and recap in validation.md are real local output, not EC2 results. Reports were written in a temporary directory within this day and removed after capture. The default remote report location remains /tmp.

Reference: [Ansible variable precedence](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html).
