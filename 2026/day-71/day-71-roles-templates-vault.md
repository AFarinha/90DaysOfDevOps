# Day 71 - Roles, Templates, Galaxy and Vault

## Implementation

The `webserver` role contains `defaults/main.yml`, `tasks/main.yml`, `handlers/main.yml`, `meta/main.yml` and three templates: `nginx.conf.j2`, `vhost.conf.j2` and `index.html.j2`. Defaults expose the application name, port, environment and worker connection limit. Callers can override defaults; role `vars/` would have higher precedence and is intentionally unnecessary here. Templates and static files do not require a `main.yml`: Ansible looks them up by filename.

`site.yml` combines the web role, `geerlingguy.docker` on app hosts, and a protected database template. `template-demo.yml`, `docker-setup.yml` and `db-setup.yml` demonstrate the individual concepts. Inventory addresses are TEST-NET placeholders and must be replaced before remote execution. This implementation targets Ubuntu; its main Nginx configuration uses the `www-data` worker account.

## Templates and rendered output

The vhost renders the port, hostname and `/var/www/terraweek` document root. The index renders host facts and the environment. The full configuration includes MIME types and all `conf.d` sites, and is checked using `nginx -t` before service changes.

The local container returned:

```html
<h1>terraweek</h1>
<p>Environment: development</p>
<p>Managed by Ansible</p>
```

The hostname and IP were also rendered from real container facts. Host facts are ephemeral and are not treated as production server evidence.

## Galaxy

Installed `geerlingguy.docker` 7.4.1 and `geerlingguy.ntp` 4.0.1 in `.cache/roles`. Installed `community.docker` 5.3.0 in `.cache/collections`. `requirements.yml` makes dependencies repeatable and records their versions. The Docker role playbook passed syntax validation and the Galaxy role executed in the disposable Ubuntu target: `ok=12 changed=3 failed=0 skipped=13`. It installed Docker packages and the Compose plugin with daemon service management disabled. Fresh VM daemon boot/service behavior remains untested.

## Vault workflow

`group_vars/db/vault.yml` is a real Vault-encrypted file containing placeholders only. Its local password is ignored under `.runtime/`; it is never copied into Markdown. Replace placeholders with actual values using `ansible-vault edit`, and supply the password through a protected CI secret or password file. Create starts an encrypted file in an editor; edit decrypts in memory for changes; view displays decrypted data; encrypt transforms plaintext into ciphertext; decrypt writes plaintext and must only be used in a private temporary location. Do not print real decrypted values into CI logs.

A password file enables unattended automation, but does not make the password intrinsically safer: permissions and secret delivery remain necessary. Database rendering uses `no_log: true`, `diff: false` and file mode `0600`, so `--diff` cannot reveal credentials.

## Validation and lessons

Four playbooks passed `--syntax-check`. The web role ran against an isolated Ubuntu 24.04 Docker container; `nginx -t` succeeded and HTTP returned the rendered page. The final repeated run reported `ok=7 changed=0 failed=0 skipped=1`. Service management was skipped because the container has no systemd; Nginx was started and reloaded explicitly for validation. Initial attempts revealed missing sudo and string-valued extra vars; the lab connection now disables become and conditionals use `| bool`.

Roles package reusable configuration; playbooks orchestrate hosts and roles; ad-hoc commands are useful for one-off inspection. Do not turn repeated multi-step configuration into ad-hoc shell commands.

## Limits and cleanup

Remote SSH hosts and real credentials were not supplied. No cloud infrastructure was created. The database placeholder template also ran locally, its secret-presence assertion passed and `/etc/db-config.env` had mode `600`. Real remote database host execution remains untested. Local cleanup is recorded in `validation.md`.
