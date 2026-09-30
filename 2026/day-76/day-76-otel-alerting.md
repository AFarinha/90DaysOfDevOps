# Day 76 - OpenTelemetry and Alerting

## Source and repeatability

The application source comes from `LondheShubham153/observability-for-devops`, verified at commit `5be5f751109bb2e185c2ac85dd3cda8015e8c60b`. Clone it into the ignored `.reference/` directory before building. The original Django app does not expose `/metrics`; `app/metrics.py` adds a counter and uptime gauge using Django and Python only. `app/start-app.py` enables that middleware without modifying upstream source. This is learning instrumentation, not a production metrics SDK.

Each day has its own `observability-stack/` snapshot and Compose project name. Run one snapshot at a time because the published ports overlap. All published endpoints bind to loopback. Grafana reads its locally generated password from an ignored `.env`; `env.sample` documents the variable without a real password. Images using `latest` are lab defaults, not reproducible production pins.

## Collector and spans

The collector receives OTLP over gRPC 4317 and HTTP 4318, batches telemetry, exposes metrics on 8889 and sends traces/logs to a detailed debug exporter. Receivers ingest, processors transform and exporters deliver. OpenTelemetry is a telemetry framework; it is not the persistent database or dashboard backend.

`send-telemetry.py` generates current timestamps, a synthetic 150ms server span and a 100ms child database span sharing a trace ID, plus the cumulative `test_requests_total` counter with value 42. Synthetic spans demonstrate serialization and parent/child relationships; they are not instrumentation of a real request through Django.

The OTLP POSTs returned HTTP 200 and the collector debug logs displayed both span names and the expected parent ID. Detailed results are in `validation.md`. In production, export to Tempo/Jaeger and protect OTLP endpoints; debug output is ephemeral and can reveal telemetry attributes.

## Alert rules

| Rule | Condition / pending period |
| --- | --- |
| HighCPUUsage | Per-instance usage above 80% for 2 minutes |
| HighMemoryUsage | Used memory above 85% for 2 minutes |
| ContainerDown | Application container series absent for 1 minute |
| TargetDown | Scrape failure for 1 minute |
| HighDiskUsage | Root filesystem usage above 90% for 5 minutes |

The `for` duration moves an alert from inactive to pending to firing and filters brief spikes. A unit test verifies TargetDown's labels, annotations and firing state. Container metadata labels match Compose service labels instead of relying on a fixed global container name.

Prometheus evaluates metric rules and needs Alertmanager to route notifications. Grafana's provisioned High Container Memory rule evaluates a 100 MiB threshold for 2 minutes and can use its own notification policies. The user chose a contact-point template without a recipient. `grafana/contact-points.yml.sample` shows email and critical-severity routing, but is deliberately not mounted into active provisioning. SMTP, real contact details and actual delivery remain unconfigured.

## Architecture and validation

```text
Notes app /metrics --------> Prometheus <-------- Node Exporter, cAdvisor
OTLP curl -> OTEL Collector -> :8889 -> Prometheus -> Grafana dashboards
OTLP curl -> OTEL Collector -> debug spans (no persistent trace backend)
Docker log API -> Promtail -> Loki -> Grafana logs
Prometheus -> alert states; Grafana -> alert evaluation -> optional contacts
```
Compose validation, Prometheus config/rule validation, OTLP ingestion, Grafana rule provisioning and the TargetDown unit test passed. Runtime state changes are documented in `validation.md`. The collector has no persistent trace backend; no notification was sent.
