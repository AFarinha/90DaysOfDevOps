# Day 77 - Integrated Observability Project

## Source and repeatability

The application source comes from `LondheShubham153/observability-for-devops`, verified at commit `5be5f751109bb2e185c2ac85dd3cda8015e8c60b`. Clone it into the ignored `.reference/` directory before building. The original Django app does not expose `/metrics`; `app/metrics.py` adds a counter and uptime gauge using Django and Python only. `app/start-app.py` enables that middleware without modifying upstream source. This is learning instrumentation, not a production metrics SDK.

Each day has its own `observability-stack/` snapshot and Compose project name. Run one snapshot at a time because the published ports overlap. All published endpoints bind to loopback. Grafana reads its locally generated password from an ignored `.env`; `env.sample` documents the variable without a real password. Images using `latest` are lab defaults, not reproducible production pins.

## Architecture

```text
Notes app /metrics --------> Prometheus <-------- Node Exporter, cAdvisor
OTLP curl -> OTEL Collector -> :8889 -> Prometheus -> Grafana dashboards
OTLP curl -> OTEL Collector -> debug spans (no persistent trace backend)
Docker log API -> Promtail -> Loki -> Grafana logs
Prometheus -> alert states; Grafana -> alert evaluation -> optional contacts
```
The stack contains eight services: Prometheus, Node Exporter, cAdvisor, Grafana, Loki, Promtail, OTEL Collector and the notes app. The final scrape configuration has five jobs because the app is instrumented as well as the four reference jobs. There are no global container names, allowing project-level isolation.

## Comparison with the reference

| Component | Reference | Implemented change |
| --- | --- | --- |
| Prometheus | Four jobs, no alert rule file | Added application metrics, retention settings and five alerts |
| Notes app | Django app without /metrics | Added dependency-free learning middleware and runtime wrapper |
| cAdvisor | Docker socket/sys/rootfs | Added containerd metadata mount for Docker 29; host UI moved to 18082 |
| Loki | TSDB v13, filesystem, single instance | Preserved the storage approach |
| Promtail | Static JSON file glob with job label | Docker discovery, project filter, container_name label and persistent positions |
| OTEL | OTLP metrics and debug traces | Preserved pipelines; test payloads use current timestamps |
| Grafana | Datasources and dashboard provider | Added fixed UIDs, 11-panel Production Overview and alert provisioning |
| Compose | Latest images, fixed container names | Project-scoped names, loopback ports and local password environment |

## Handoff and runtime evidence

Start from `tasks.md`, validate config, launch the stack, generate notes API traffic and run the telemetry script. `validation.md` records API responses, query results and startup corrections. The final target check reported all five jobs UP. Grafana 13.2.3 reported its database healthy; both datasources, the 11-panel dashboard and High Container Memory alert rule were retrieved through authenticated API calls. Five LogQL queries returned real log lines. The debug exporter showed both synthetic spans.

The original app scrape returned 404 before instrumentation. An unavailable disk mount and an occupied 8080 host port were corrected for cAdvisor. An early target snapshot is retained alongside the corrected final snapshot instead of presenting the initial failures as successes.

## Production readiness

The lab is an integrated learning setup, not an HA production deployment. Add Alertmanager routing, Grafana Tempo, TLS/authentication, external credentials, lifecycle-supported log collection, explicit image digests, Loki retention and object storage, backup/restore testing, dashboard review and capacity planning. Node Exporter observes WSL/Linux, not Windows host resources. Docker socket access remains privileged even with a read-only mount.

Self-hosting provides control and open query formats, but requires operating storage, upgrades and reliability. Managed services reduce that operational burden at the cost of billing and provider integration decisions. No price comparison was attempted.

| Day | Concept applied |
| --- | --- |
| 73 | Metrics, counters/gauges and PromQL |
| 74 | Host/container exporters and provisioned dashboards |
| 75 | Logs, bounded labels and LogQL |
| 76 | OTLP pipelines, spans and alert evaluation |
| 77 | End-to-end integration, corrections and handoff |

Cleanup is recorded in `validation.md`; no existing cluster or unrelated container is a cleanup target.
