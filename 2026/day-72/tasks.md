# Day 72 Commands

Run from this day directory, then enter the project as shown. Remote deployment and the disposable local lab are alternatives. Real secrets/password files must be provisioned privately.

| Command | What it does |
| --- | --- |
| `cd ansible-docker-project` | Enter the project; subsequent commands run here. |
| `export PATH="$HOME/.local/share/devops-ansible/bin:$PATH"` | Use the existing user-local Ansible tools. |
| `ansible-galaxy collection install -r requirements.yml -p ../.cache/collections` | Install required, pinned Docker and timezone collections locally. |
| `ansible-vault edit group_vars/web/vault.yml` | Privately replace encrypted credentials; an empty username skips login. |
| `ansible-playbook site.yml --syntax-check --vault-password-file ../.runtime/vault-pass` | Parse the project with its encrypted placeholder configuration. |
| `ansible-playbook site.yml --check --diff --ask-vault-pass` | Remote preview; modules depending on newly installed packages may not simulate a fresh VM fully. |
| `ansible-playbook site.yml --ask-vault-pass` | Remote deployment: installs packages, changes baseline settings and runs containers. |
| `ansible-playbook site.yml --tags docker --ask-vault-pass` | Only execute Docker tasks. |
| `ansible-playbook site.yml --tags nginx --ask-vault-pass` | Only render/test/reload the proxy. |
| `ansible-playbook site.yml --skip-tags common --ask-vault-pass` | Deploy app and proxy without baseline server changes. |
| `docker run -d --name day72-server --network host -v /var/run/docker.sock:/var/run/docker.sock ubuntu:24.04 sleep infinity` | Create trusted disposable target; the Docker socket exposes the host daemon and host networking shares its loopback. |
| `docker exec day72-server bash -lc "apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3 python3-requests nginx sudo"` | Bootstrap packages in the disposable target only. |
| `ansible-playbook site.yml -i inventory.lab.ini --vault-password-file ../.runtime/vault-pass -e lab_mode=true -e docker_app_name=day72-app -e docker_app_port=18081 -e nginx_http_port=18080` | Lab deployment; repeat this exact command to check idempotency. VM-only steps are skipped. |
| `docker exec day72-server nginx` | Start the lab proxy after its first deployment. |
| `docker exec day72-server nginx -s reload` | Reload the lab proxy after template changes. |
| `curl --fail http://127.0.0.1:18081` | Verify the application directly on loopback. |
| `curl --fail http://127.0.0.1:18080` | Verify the same application through the proxy. |
| `docker ps --filter name=day72-app` | Inspect the exact lab application container and mapping. |
| `ansible-playbook site.yml --tags docker --ask-vault-pass -e docker_app_image=httpd -e docker_app_tag=alpine` | Remote bonus alternative: retain the stable container name while replacing its image. |
| `docker rm -f day72-app day72-server` | Cleanup: deletes only the lab application and disposable target; do not use on reused names. |
