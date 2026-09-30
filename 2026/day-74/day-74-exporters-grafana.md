# Day 74 - Exporters and Grafana

## Source and repeatability

The application source comes from `LondheShubham153/observability-for-devops`, verified at commit `5be5f751109bb2e185c2ac85dd3cda8015e8c60b`. Clone it into the ignored `.reference/` directory before building. The original Django app does not expose `/metrics`; `app/metrics.py` adds a counter and uptime gauge using Django and Python only. `app/start-app.py` enables that middleware without modifying upstream source. This is learning instrumentation, not a production metrics SDK.

Each day has its own `observability-stack/` snapshot and Compose project name. Run one snapshot at a time because the published ports overlap. All published endpoints bind to loopback. Grafana reads its locally generated password from an ignored `.env`; `env.sample` documents the variable without a real password. Images using `latest` are lab defaults, not reproducible production pins.

## Exporters and host scope

Node Exporter reads `/proc`, `/sys` and the filesystem read-only, reporting host CPU, memory, disk and network metrics. In this WSL environment the host is Linux/WSL, not the Windows desktop. cAdvisor reads cgroups, Docker metadata and containerd metadata to report container usage. Docker 29 uses containerd-backed image storage here, so its socket directory is also mounted. cAdvisor's UI uses loopback port 18082 to avoid a pre-existing listener on 8080; its internal metrics endpoint stays on 8080.

A read-only mount of a Docker socket does not make the Docker API read-only. Restrict exporter access and host mounts in production.

## Dashboards as code

`grafana/provisioning/datasources/datasources.yml` supplies a fixed Prometheus datasource UID. The dashboard provider loads `grafana/dashboards/overview.json` automatically. The overview includes CPU/memory gauges, container CPU time series, container memory and root filesystem usage. Provisioning makes a clean deployment reproduce the same sources and panels.

Requested community dashboards 1860 (Node Exporter Full) and 193 (Docker monitoring) were downloaded from Grafana's dashboard API and saved as JSON with the Prometheus input resolved. Compatibility depends on their queries matching the exported labels; they are community dashboards, not a guarantee that every panel works unchanged.

| Query | Meaning |
| --- | --- |
| `100-avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))*100` | Host CPU usage percentage |
| `(1-node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes)*100` | Host used memory percentage |
| `(1-node_filesystem_avail_bytes{mountpoint="/"}/node_filesystem_size_bytes{mountpoint="/"})*100` | Root filesystem usage |
| `rate(container_cpu_usage_seconds_total{name!=""}[5m])*100` | Container CPU percentage of a CPU core; values may exceed 100 on multicore workloads |
| `container_memory_usage_bytes{name!=""}/1024/1024` | Container memory in MiB |

## Validation

Compose passed validation. The integrated runtime exposed real host metrics and 12 named container memory series; dashboards and datasource APIs were checked. Day-specific checks and cleanup are in `validation.md`. Provisioning evidence is stored as text; screenshots were excluded as requested.
