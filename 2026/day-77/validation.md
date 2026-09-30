# Day 77 Runtime Validation

Executed on 2026-09-30 in an isolated Docker Compose project.

## Targets

```json
[
  {
    "job": "cadvisor",
    "health": "down",
    "error": "Get \"http://cadvisor:8080/metrics\": dial tcp: lookup cadvisor on 127.0.0.11:53: no such host"
  },
  {
    "job": "node-exporter",
    "health": "up",
    "error": ""
  },
  {
    "job": "notes-app",
    "health": "up",
    "error": ""
  },
  {
    "job": "otel-collector",
    "health": "up",
    "error": ""
  },
  {
    "job": "prometheus",
    "health": "up",
    "error": ""
  }
]
```

## Grafana health

```json
{
  "database": "ok",
  "version": "13.2.3",
  "commit": "90ffed056f0884267356c12a0eeb72a022af53f1",
  "enterpriseCommit": "ff58d02cd1a8decff90a1d5994d145f9f9c3be0f"
}
```

## Datasources

```json
[
  {
    "name": "Loki",
    "type": "loki",
    "url": "http://loki:3100"
  },
  {
    "name": "Prometheus",
    "type": "prometheus",
    "url": "http://prometheus:9090"
  }
]
```

## Dashboard

```json
{
  "title": "Production Overview -- Observability Stack",
  "panels": 11
}
```

## Grafana alert rules

```json
[
  {
    "title": "High Container Memory",
    "uid": "container-memory",
    "for": "2m"
  }
]
```

## Loki labels

```json
{
  "status": "success",
  "data": [
    "container_name",
    "job",
    "service_name"
  ]
}
```

## Executed queries

| Query | Result |
| --- | --- |
| `up` | 5 series; 1, 1, 1, 1, 1 |
| `count({__name__=~".+"})` | 1 series; 7571 |
| `process_resident_memory_bytes` | 3 series; 21917696, 235827200, 87523328 |
| `prometheus_http_requests_total` | 64 series; 0, 0, 0, 0, 0 |
| `rate(prometheus_http_requests_total{code!="200"}[5m])` | 0 series;  |
| `100 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100` | 1 series; 16.178508771929785 |
| `(1-node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes)*100` | 1 series; 20.55633239324477 |
| `count(container_memory_usage_bytes{name!=""})` | 1 series; 12 |
| `test_requests_total` | 0 series;  |
| `notes_http_requests_total` | 1 series; 0 |
| `{job="docker"}` | {"streams": 1, "lines": 5} |
| `{container_name="notes-app"}` | {"streams": 1, "lines": 5} |
| `{job="docker"} \|= "error"` | {"streams": 1, "lines": 5} |
| `{job="docker"} != "health"` | {"streams": 1, "lines": 5} |
| `{job="docker"} \|~ "GET"` | {"streams": 1, "lines": 5} |

## Targets after startup corrections

```json
[
  {
    "job": "cadvisor",
    "health": "up",
    "error": ""
  },
  {
    "job": "node-exporter",
    "health": "up",
    "error": ""
  },
  {
    "job": "notes-app",
    "health": "up",
    "error": ""
  },
  {
    "job": "otel-collector",
    "health": "up",
    "error": ""
  },
  {
    "job": "prometheus",
    "health": "up",
    "error": ""
  }
]
```

## OTLP metric after batch and scrape

```json
[
  {
    "metric": {
      "__name__": "test_requests_total",
      "exported_job": "my-test-service",
      "instance": "otel-collector:8889",
      "job": "otel-collector"
    },
    "value": [
      1790781425.986,
      "42"
    ]
  }
]
```

## Intentional app fault

```json
[
  {
    "alert": "TargetDown",
    "job": "notes-app",
    "state": "firing"
  }
]
```

Recovery: `up{job="notes-app"}` = 1

## Cleanup

All task-created lab containers, Compose networks/volumes and Helm releases were removed. The disposable namespace was deleted; the pre-existing devops-cluster was preserved. Dependencies, reference sources and package artifacts remain only in ignored local directories.
