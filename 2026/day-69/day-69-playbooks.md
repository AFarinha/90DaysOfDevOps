# Day 69 - Ansible playbooks and modules

## Execution status

The source files are prepared. Local validation is recorded in [validation.md](validation.md). Terraform 1.13.5, AWS CLI 2.37.6 and Ansible Core 2.21.4 were installed in the Ubuntu WSL user's local directories. The STS identity check failed with "Unable to locate credentials". No AWS resources have been created, changed or destroyed in this session.

The user selected local preparation only. The cloud exercise is **pending**, not completed. No successful apply, AWS resource IDs, lock errors, SSH results or remote idempotency evidence are claimed. Text captures are used for local evidence; no screenshots were generated. Local preparation is committed separately for this day. Cloud exercise completion and push remain pending.

## Playbook structure and files

The [ansible-practice/](ansible-practice/) directory contains install-nginx.yml, essential-modules.yml, nginx-config.yml, multi-play.yml and files/app.conf plus files/nginx.conf. These target the Ubuntu lab defined for Day 68. Paths, package names and the nginx www-data user are chosen for Ubuntu rather than copying Amazon Linux defaults.

A play selects hosts and sets play-level options. Its tasks are ordered module invocations. A playbook can contain multiple plays targeting web, app and db separately. Play-level become applies to tasks by default; a task can override it. A failed task normally removes that host from later tasks in the play while other hosts continue, unless explicit error handling changes this behavior.

## Essential modules

| Module | Example and purpose |
| --- | --- |
| apt | Install utilities; optional tagged tree removal demonstrates state=absent. |
| service | Start/enable Nginx only in web. |
| copy | Deploy app.conf and Nginx configuration with explicit file modes. |
| file | Create /opt/myapp with ownership and permissions. |
| command | Read disk space without a shell. |
| shell | Count processes through a pipeline. |
| lineinfile | Replace one TZ line rather than appending duplicates. |

Read-only command/shell tasks use changed_when=false so diagnostic activity does not obscure idempotency.

## Nginx and handlers

install-nginx.yml installs and enables Nginx and replaces Ubuntu's default index page. nginx-config.yml validates the candidate config using nginx -t before deploying it. A changed config notifies Restart Nginx; the handler runs once at the end of the play. The expected first run triggers it and an unchanged second run does not. This expectation has not been verified on EC2.

multi-play.yml installs Nginx only on web, build tools on app and the MySQL client on db, with separate directories. List-hosts/list-tasks validation checks intended targeting but does not prove installed package isolation.

## Preview flags and evidence

--check predicts changes where modules support check mode; --diff shows supported file differences and can expose sensitive content; -v through -vvv increases diagnostic detail. --limit restricts target hosts; --list-hosts and --list-tasks list scope without modifying it. Check mode is valuable but cannot guarantee runtime success.

All playbooks were syntax-checked. Local diagnostic tasks and target lists are recorded in validation.md. Actual package installation, HTTP validation, two Nginx runs and handler/idempotency results remain pending remote servers.
