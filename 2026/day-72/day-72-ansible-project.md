# Day 72 - Docker and Nginx through Ansible

## Architecture and structure

```text
Ansible -> Ubuntu target [Nginx:80 -> 127.0.0.1:8080 -> application container:80]
```

`ansible-docker-project/` contains `ansible.cfg`, remote and lab inventories, `site.yml`, collection requirements, `group_vars/all.yml`, web variables and an encrypted placeholder vault. Each of the common, docker and nginx roles contains its task list; Docker and Nginx also have defaults, handlers and templates. The Compose template is provided for the multi-container extension; current deployment uses `docker_container`.

The common role refreshes apt metadata, installs baseline packages, configures the hostname/timezone and creates the deploy user. The Docker role adds the official Ubuntu repository and signing key, installs Docker CE and the Compose plugin, enables the daemon, configures group membership, optionally authenticates to Docker Hub, pulls an image and manages one stable container name. The Nginx role removes the Ubuntu default site, renders the main/proxy configs, tests syntax and reloads on configuration changes.

The application port binds to loopback so the public entry point is the proxy. `/health` checks Nginx itself; `/` checks the actual upstream. `nginx_upstream_port` follows `docker_app_port`, preventing a port override from silently breaking routing.

## Tags, Vault and idempotency

`common`, `docker` and `nginx` tags support selective execution. `--skip-tags common` leaves baseline configuration alone. The Docker login uses `no_log`; encrypted placeholders have an empty username so the lab performs no real login. Actual credentials must be inserted privately with Vault before a private image deployment.

The isolated lab used a disposable Ubuntu container with the host Docker socket, host networking and ports 18080/18081. `lab_mode=true` skips hostname/timezone changes and Docker daemon installation/service management, while still running the roles that manage packages, container state and proxy templates. Socket access grants Docker daemon control; this is a local trusted lab configuration, not a production remote inventory pattern.

The deploy succeeded and HTTP through port 18080 returned the Nginx application container page. The repeated run reported `ok=18 changed=0 failed=0 skipped=7`. These numbers exclude the real VM-only steps; they do not prove fresh-server Docker installation. The earlier vault password omission was corrected by explicitly supplying the ignored password file.

The bonus run replaced the existing container with `httpd:alpine` and the unchanged Nginx proxy returned the Apache It works page.

For the alternate app exercise, keep `docker_app_name` unchanged and change only image/tag. Changing the name creates a second container and can cause a port collision; it does not replace the original container.

## Concepts and production follow-up

| Day | Applied concept |
| --- | --- |
| 68 | Inventory and connection |
| 69 | Modules, playbooks and handlers |
| 70 | Variables, conditionals and fact-based repository configuration |
| 71 | Roles, templates, collections and Vault |
| 72 | End-to-end deployment and repeated-run validation |

Production needs TLS, restricted ingress, monitoring, backups, explicit image digests, credential rotation and log retention. The deploy user and Docker group membership are privileged choices. The playbooks target Ubuntu; RHEL support is not claimed.

## Limits and cleanup

No EC2 instance or AWS resource was created. Real Docker Hub authentication, fresh-VM Docker installation and remote SSH execution remain untested. The lab uses an existing Docker daemon. Local cleanup is recorded in `validation.md`.
