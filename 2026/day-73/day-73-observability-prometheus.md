# Day 73 - Observability and Prometheus

Metrics are numeric time series, logs record events and traces connect spans across a request. Monitoring checks known conditions; observability combines these signals to investigate causes beyond a predefined alert. A database timeout can increase latency metrics, appear in an error log and lengthen a database span.

## Source and repeatability

The application source comes from `LondheShubham153/observability-for-devops`, verified at commit `5be5f751109bb2e185c2ac85dd3cda8015e8c60b`. Clone it into the ignored `.reference/` directory before building. The original Django app does not expose `/metrics`; `app/metrics.py` adds a counter and uptime gauge using Django and Python only. `app/start-app.py` enables that middleware without modifying upstream source. This is learning instrumentation, not a production metrics SDK.

Each day has its own `observability-stack/` snapshot and Compose project name. Run one snapshot at a time because the published ports overlap. All published endpoints bind to loopback. Grafana reads its locally generated password from an ignored `.env`; `env.sample` documents the variable without a real password. Images using `latest` are lab defaults, not reproducible production pins.

## Configuration and concepts

`observability-stack/prometheus.yml` scrapes Prometheus and the instrumented notes app every 15 seconds. The Compose file persists the TSDB in a named volume and limits retention to 30 days or 1GB, whichever is reached first. Expired blocks are removed; disk usage can temporarily exceed the threshold before compaction/cleanup. A volume keeps data across container replacement, but `down -v` deletes it.

A counter accumulates events, such as `notes_http_requests_total`, and may reset when a process restarts. A gauge represents a current value, such as resident memory or uptime, and can increase or decrease. Histograms expose bucket counts suitable for aggregation; summaries calculate quantiles on the client and cannot normally combine those quantiles across instances. Metric name plus labels identifies a time series; high-cardinality labels increase storage and query cost.

## Queries

| PromQL | Interpretation |
| --- | --- |
| `up` | 1 for each successful scrape, 0 for failures |
| `count({__name__=~".+"})` | Number of currently selected series, not the number of unique metric names |
| `process_resident_memory_bytes{job="prometheus"}` | Prometheus resident memory in bytes |
| `prometheus_http_requests_total` | HTTP counters partitioned by handler/code |
| `rate(prometheus_http_requests_total{code!="200"}[5m])` | Per-second rate of non-200 responses; an empty vector is possible if those series do not exist |
| `sum(rate(prometheus_http_requests_total[5m]))` | Aggregate HTTP rate, applying rate before sum so counter resets are handled per series |
| `topk(5, prometheus_http_requests_total)` | Five largest request counters |

Use instant queries for current values; `[5m]` selects a range and `rate` estimates counter change per second. Query evidence is recorded in `validation.md`; empty results are not fabricated as zero.

## Planned architecture

```text
Notes app /metrics --------> Prometheus <-------- Node Exporter, cAdvisor
OTLP curl -> OTEL Collector -> :8889 -> Prometheus -> Grafana dashboards
OTLP curl -> OTEL Collector -> debug spans (no persistent trace backend)
Docker log API -> Promtail -> Loki -> Grafana logs
Prometheus -> alert states; Grafana -> alert evaluation -> optional contacts
```
## Validation

Compose configuration passed. The final integrated stack proved the shared Prometheus/app configuration with both targets UP, and served the actual notes API. Day-specific startup and query results are recorded in `validation.md`. The complete pipeline adds logs and traces on subsequent days.
