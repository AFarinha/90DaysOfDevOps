# Day 75 Commands

Run from this day directory in WSL, then enter the stack as shown. The reference checkout is ignored. Change the local Grafana sample password privately before starting. Do not run snapshots concurrently on the same ports. Query explanations are in the main day report.

| Command | What it does |
| --- | --- |
| `git clone --depth 1 https://github.com/LondheShubham153/observability-for-devops.git .reference` | Obtain upstream sample app source in the ignored directory; omit if it already exists. |
| `cd observability-stack` | Enter this day snapshot; subsequent commands run here. |
| `cp env.sample .env` | First-run setup only: creates local configuration. Do not overwrite an existing .env. |
| `chmod 600 .env` | Restrict local password-file access; replace the sample password privately before launching. |
| `docker compose config --quiet` | Validate Compose interpolation and configuration without printing passwords. |
| `docker compose build notes-app` | Build the supplied application source; the mounted middleware adds metrics without new packages. |
| `docker compose up -d` | Launch this snapshot. Stop other snapshots first to avoid port conflicts. |
| `docker compose ps` | List project services and states. |
| `docker compose exec -T prometheus promtool check config /etc/prometheus/prometheus.yml` | Check Prometheus config; -T avoids allocating a terminal. |
| `curl --fail http://127.0.0.1:8000/api/notes/` | Verify application API and generate a request. |
| `curl --fail http://127.0.0.1:8000/metrics` | Inspect the real application counter/gauge. |
| `curl --fail --get http://127.0.0.1:9090/api/v1/query --data-urlencode query=up` | Run a PromQL query; --get and URL encoding preserve the expression. |
| `docker compose exec -T prometheus du -sh /prometheus` | Inspect TSDB disk usage. |
| `curl --fail http://127.0.0.1:9100/metrics` | Check Linux host metrics. |
| `curl --fail http://127.0.0.1:18082/metrics` | Check cAdvisor through its alternate loopback port. |
| `curl --fail http://127.0.0.1:3000/api/health` | Check Grafana database/version; dashboard/source details require local authentication. |
| `curl --fail http://127.0.0.1:3100/ready` | Check Loki readiness. |
| `curl --fail http://127.0.0.1:9080/targets` | Inspect Promtail discovery. |
| `curl --fail --get http://127.0.0.1:3100/loki/api/v1/query_range --data-urlencode 'query={container_name="notes-app"}' --data-urlencode limit=5` | Retrieve five application log lines. |
| `docker compose restart grafana` | Reload provisioning after datasource/dashboard changes. |
| `docker compose logs --tail 30` | Troubleshoot startup failures without dumping unlimited logs; do not publish real secrets. |
| `docker compose down` | Stop/remove this project containers/network while preserving data. |
| `docker compose down -v` | Destructive alternative cleanup: also deletes this project TSDB, logs, dashboard data and positions. Use only for disposable lab data. |
