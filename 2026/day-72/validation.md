# Day 72 Validation

Executed on 2026-09-30 using isolated Ubuntu containers.

## deploy.txt

```text
day72-server               : ok=18   changed=8    unreachable=0    failed=0    skipped=8    rescued=0    ignored=0
```

## idempotency.txt

```text
day72-server               : ok=18   changed=0    unreachable=0    failed=0    skipped=7    rescued=0    ignored=0
```

## bonus.txt

```text
day72-server               : ok=8    changed=2    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0
```

- Project syntax check passed.
- Application HTTP and proxy HTTP returned success.
- The repeat run had changed=0 and failed=0.
- Real Docker Hub login and fresh VM daemon/service setup were not exercised.

Bonus: replaced day72-app with httpd:alpine using the same container name and ports; proxy returned the Apache It works page.

## Cleanup

All task-created lab containers, Compose networks/volumes and Helm releases were removed. The disposable namespace was deleted; the pre-existing devops-cluster was preserved. Dependencies, reference sources and package artifacts remain only in ignored local directories.
