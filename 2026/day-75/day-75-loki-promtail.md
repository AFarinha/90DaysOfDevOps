# Day 75 - Loki and Promtail

## Source and repeatability

The application source comes from `LondheShubham153/observability-for-devops`, verified at commit `5be5f751109bb2e185c2ac85dd3cda8015e8c60b`. Clone it into the ignored `.reference/` directory before building. The original Django app does not expose `/metrics`; `app/metrics.py` adds a counter and uptime gauge using Django and Python only. `app/start-app.py` enables that middleware without modifying upstream source. This is learning instrumentation, not a production metrics SDK.

Each day has its own `observability-stack/` snapshot and Compose project name. Run one snapshot at a time because the published ports overlap. All published endpoints bind to loopback. Grafana reads its locally generated password from an ignored `.env`; `env.sample` documents the variable without a real password. Images using `latest` are lab defaults, not reproducible production pins.

## Log pipeline

```text
Docker containers -> Docker log API -> Promtail -> Loki -> Grafana Explore/dashboard
```

Loki stores compressed log chunks and indexes labels. This lowers indexing cost, but a text search still scans matching streams. Elasticsearch is preferable when richer indexed full-text searches are central to the workload. Keep labels such as service/container/job bounded; request IDs should stay in log content rather than labels.

`loki/loki-config.yml` uses single-tenant, local filesystem storage, TSDB index schema v13 and replication factor 1. It is a single-instance lab configuration. `promtail/promtail-config.yml` discovers Docker containers, filters the current Compose project and relabels the Compose service as `container_name`. This fixes the reference's static-file configuration, which did not supply the label used in the exercises. The position file persists in a named volume.

Promtail has reached end of life as of 2026-03-02. It is retained to execute this challenge, while a production migration should use Grafana Alloy. [Official lifecycle notice](https://grafana.com/docs/loki/latest/send-data/promtail/).

## LogQL and correlation

| Query | Meaning |
| --- | --- |
| `{job="docker"}` | All streams for this Compose project |
| `{container_name="notes-app"}` | Application logs |
| `{job="docker"} |= "error"` | Case-sensitive error substring |
| `{job="docker"} != "health"` | Exclude health-check noise |
| `{job="docker"} |~ "GET"` | Regex match of HTTP request lines |
| `sum(count_over_time({container_name="notes-app"} |~ "(?i)error" [1m]))` | Count error lines per minute |
| `sum by(container_name)(rate({job="docker"}[5m]))` | Per-container log rate |

For error logs in the last hour, set Grafana Explore's time range to Last 1 hour and run `{container_name="notes-app"} |~ "(?i)error"`. The range selector is used for log metric calculations, not as a replacement for the UI log-query time range.

The dashboard has a Loki logs panel. Explore split view can align a Prometheus CPU query with app logs at the same timestamp; the correlation shows co-occurrence and is not automatic proof of causation.

## Validation

Compose passed. Loki returned labels `container_name`, `job` and `service_name`. Five LogQL queries executed on the final stack and each returned five sample lines under the requested limit. That does not establish the total log count. Day-specific startup and cleanup evidence is in `validation.md`.
