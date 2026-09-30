# Day 68 - Ansible introduction and inventory

## Execution status

The source files are prepared. Local validation is recorded in [validation.md](validation.md). Terraform 1.13.5, AWS CLI 2.37.6 and Ansible Core 2.21.4 were installed in the Ubuntu WSL user's local directories. The STS identity check failed with "Unable to locate credentials". No AWS resources have been created, changed or destroyed in this session.

The user selected local preparation only. The cloud exercise is **pending**, not completed. No successful apply, AWS resource IDs, lock errors, SSH results or remote idempotency evidence are claimed. Text captures are used for local evidence; no screenshots were generated. Local preparation is committed separately for this day. Cloud exercise completion and push remain pending.

## Architecture and configuration management

Configuration management keeps packages, users, files and services in a repeatable desired state after servers exist. Terraform provisions the machines; Ansible configures them. The control node runs Ansible, reads inventory and playbooks, and executes modules on managed nodes over SSH. Most POSIX modules need Python on the targets; no persistent Ansible agent is required.

Chef and Puppet commonly use installed agents and a central service. Salt supports master/minion and agentless modes. Ansible's normal SSH model is useful when standard SSH access already exists.

## Lab design and inventory

The prepared [terraform-lab/](terraform-lab/) provisions three Ubuntu 22.04 t2.micro instances named web/app/db in a dedicated public subnet. An existing AWS key pair and a control-node IPv4 /32 are required. HTTP and SSH access are limited to that address. AWS provisioning has not run.

[ansible-practice/inventory.ini](ansible-practice/inventory.ini) uses reserved documentation addresses 192.0.2.10-12. Replace them in ignored inventory.local.ini using real outputs and an external private key. No SSH key is stored in the repository. host_key_checking remains enabled; verify server fingerprints when first connecting.

The application group contains web+app; all_servers contains application+db. The configured default inventory removes the need to repeat -i. Explicit -i inventory-local.ini is used only for local verification.

## Executed local evidence

The separate inventory-local.ini assigns all three aliases to the same WSL host with ansible_connection=local. Ping, group patterns, uptime, memory, disk, copying hello.txt and reading its contents ran locally; exact output and exit codes are in validation.md. Package installation on a managed node and remote SSH connectivity were not executed.

| Exercise | Result interpretation |
| --- | --- |
| ping | Tests Ansible/Python execution, not ICMP reachability. |
| uptime | Reads host uptime and load. |
| free -h | Reads memory in human-readable units. |
| df -h / | Reads root filesystem usage. |
| copy and cat | Transfer and read back a temporary file; local files were cleaned up. |

become escalates privilege, usually through sudo, for package installation or protected system files. command executes arguments without pipes or redirects. shell invokes a shell for those operators and needs careful quoting. Read-only commands can report changed by default unless changed_when is overridden in a playbook.
