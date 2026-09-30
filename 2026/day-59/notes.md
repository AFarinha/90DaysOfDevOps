# Day 59 Notes

Installed Helm v4.3.0 locally. Deployed Bitnami nginx 25.2.1, customized with CLI and values, scaled 1 -> 5 -> 1 through upgrade/rollback, and tested a custom nginx:1.25 chart at three and five replicas.

All exercise manifests were validated with client and server dry-runs. See [day-59-helm.md](day-59-helm.md) for concepts and limitations, [tasks.md](tasks.md) for explained commands and [validation.md](validation.md) for real execution evidence. No credentials or screenshots are stored.
