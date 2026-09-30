# Day 54 - ConfigMaps and Secrets

## Configuration without rebuilding images

ConfigMaps hold non-sensitive text settings or files; Secrets hold sensitive values with separate access control. app-config contained APP_ENV=production, APP_DEBUG=false and APP_PORT=8080. nginx-config was created from [default.conf](default.conf), whose /health location returns healthy.

[config-env-pod.yaml](config-env-pod.yaml) injects all app-config keys through envFrom. Its logs printed the three expected values. [nginx-config-pod.yaml](nginx-config-pod.yaml) mounts the ConfigMap as /etc/nginx/conf.d/default.conf; its local HTTP health check returned healthy.

## Secret consumption and encoding

The temporary db-credentials Secret used an admin username and a randomly generated password rather than the README's example password. The password was never printed or stored in the repository. [secret-pod.yaml](secret-pod.yaml) uses secretKeyRef for DB_USER and mounts both keys read-only under /etc/db-credentials. Checks confirmed the username matched and the password file was nonempty.

The API data fields are base64-encoded. Decoding them in memory succeeded. Encoding is reversible without a key; it is not encryption. Protect Secrets with least-privilege RBAC and encryption at rest. Avoid dumping full Secret YAML into logs or documentation.

## Updates and propagation

Environment variables are established when a container starts and do not change when the ConfigMap changes. Projected volumes refresh eventually through the kubelet, with a delay affected by sync and cache settings. A subPath mount does not receive those refreshes.

[live-config-pod.yaml](live-config-pod.yaml) reads the projected message file every five seconds. Patching hello to world changed its logs without restarting the Pod: the readiness listing showed restart count zero. This run observed propagation within the bounded polling loop; do not assume a universal 30-60 second guarantee.

## Validation and cleanup

All four Pod manifests passed client and server dry-runs. Environment, file, HTTP, base64 and live-update checks succeeded. The four Pods, three ConfigMaps and Secret were deleted. See [tasks.md](tasks.md) and [validation.md](validation.md).
