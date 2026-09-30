# Day 71 Commands

Run from this day directory in WSL. Remote and local laboratory execution are alternatives. The shipped vault contains placeholders and its ignored local password file is not distributed. For another checkout, recreate the placeholder vault with a new password.

| Command | What it does |
| --- | --- |
| `export PATH="$HOME/.local/share/devops-ansible/bin:$PATH"` | Use the existing user-local Ansible installation in this environment. |
| `ansible-galaxy role install -r requirements.yml -p .cache/roles` | Install the pinned community roles into the ignored local cache. |
| `ansible-galaxy collection install -r requirements.yml -p .cache/collections` | Install the Docker connection collection locally. |
| `ansible-galaxy role list -p .cache/roles` | List installed roles and versions. |
| `ansible-galaxy search nginx --platforms EL` | Search Galaxy; an alternative discovery command, not required for deployment. |
| `ansible-galaxy search mysql` | Search database roles. |
| `ansible-galaxy init .runtime/role-skeleton` | Explore a temporary role skeleton without overwriting the implemented role. |
| `ansible-playbook site.yml --syntax-check --vault-password-file .runtime/vault-pass` | Parse roles and playbook using the local placeholder vault. |
| `ansible-playbook template-demo.yml --check --diff` | Preview non-secret web configuration on configured remote inventory hosts. |
| `ansible-playbook site.yml --ask-vault-pass` | Deploy to configured remote hosts; modifies packages, services and configuration. |
| `ansible-playbook docker-setup.yml` | Install Docker on configured app hosts; requires privileged access. |
| `ansible-vault edit group_vars/db/vault.yml` | Replace encrypted placeholders privately using the current vault password. |
| `ansible-vault create .runtime/secrets.yml` | Create a new encrypted scratch file; interactive editor and password prompt. |
| `ansible-vault view .runtime/secrets.yml` | View scratch values privately; never copy real secrets into logs. |
| `ansible-vault decrypt .runtime/secrets.yml` | Writes plaintext: only use for disposable placeholder data inside the ignored scratch directory. |
| `ansible-vault encrypt .runtime/secrets.yml` | Encrypt the disposable plaintext file again. |
| `ansible-playbook db-setup.yml --ask-vault-pass` | Assert secret presence without printing it. |
| `docker run -d --name day71-web -p 127.0.0.1:18071:80 ubuntu:24.04 sleep infinity` | Create a temporary web target, with HTTP bound to loopback. |
| `docker exec day71-web bash -lc "apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3 nginx"` | Bootstrap the disposable target; installs packages only inside it. |
| `ansible-playbook site.yml -i inventory.lab.ini --limit web -e manage_service=false` | Apply only the web role to the lab, skipping systemd management. |
| `docker exec day71-web nginx` | Start Nginx explicitly in the lab container. |
| `docker exec day71-web nginx -s reload` | Reload after a repeated role run; use instead of starting another Nginx process. |
| `curl --fail -H Host:terraweek http://127.0.0.1:18071` | Verify the custom page; --fail rejects HTTP error responses. |
| `docker rm -f day71-web` | Cleanup: deletes only the disposable web container. Do not reuse its name for unrelated work. |

## Additional validated local flows

| Command | What it does |
| --- | --- |
| `ansible-playbook site.yml -i inventory.db-lab.ini --limit db --vault-password-file .runtime/vault-pass` | Render encrypted placeholders on the temporary DB target without logging their values. |
| `docker exec day71-web stat -c %a /etc/db-config.env` | Verify the database config mode is 600. |
| `ansible-playbook docker-setup.yml -i inventory.app-lab.ini -e '{"docker_service_manage": false, "docker_install_compose": false}'` | Apply the installed Galaxy role to the day-72 disposable target; installs packages but does not manage the host Docker daemon. |
