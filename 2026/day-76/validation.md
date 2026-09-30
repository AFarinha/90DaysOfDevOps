# Day 76 Validation

Executed on 2026-09-30; each snapshot was launched independently.

- docker tag day77-notes-app:lab day76-notes-app:lab: exit 0
- docker compose config --quiet: exit 0
- docker compose up -d --no-build: exit 0

Targets after the first scrape:

```json
[
  [
    "cadvisor",
    "up"
  ],
  [
    "node-exporter",
    "up"
  ],
  [
    "notes-app",
    "up"
  ],
  [
    "otel-collector",
    "up"
  ],
  [
    "prometheus",
    "up"
  ]
]
```

Prometheus validation:

```text
Checking /etc/prometheus/prometheus.yml
  SUCCESS: 1 rule files found
 SUCCESS: /etc/prometheus/prometheus.yml is valid prometheus config file syntax

Checking /etc/prometheus/alert-rules.yml
  SUCCESS: 5 rules found
```

Cleanup: project containers, network and named volumes removed; exit 0.

## Cleanup

All task-created lab containers, Compose networks/volumes and Helm releases were removed. The disposable namespace was deleted; the pre-existing devops-cluster was preserved. Dependencies, reference sources and package artifacts remain only in ignored local directories.
