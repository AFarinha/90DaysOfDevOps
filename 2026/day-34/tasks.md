# Tasks - Day 34

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-34/compose-app-stack` | Changes into the Compose project directory before running stack commands. |
| `docker compose config` | Validates and renders the final Compose configuration after variable interpolation. |
| `docker compose up --build -d` | Builds the custom web app image and starts all services in detached mode. |
| `docker compose ps` | Shows the state and health of the running services. |
| `docker compose logs -f web` | Follows logs from the web service to confirm it waited for dependencies and started correctly. |
| `curl http://localhost:8081` | Sends a request to the Flask app through the mapped host port. |
| `curl http://localhost:8081/health` | Checks the app health endpoint, including database and Redis connectivity. |
| `docker compose kill db` | Stops the database container abruptly to test the `restart: always` policy. |
| `docker compose ps db` | Checks whether the database container restarted after being killed. |
| `docker compose up --build -d web` | Rebuilds and restarts the web service after an app code change. |
| `docker compose up -d --scale web=3` | Attempts to run three web replicas to observe scaling behaviour with host port mapping. |
| `docker compose down` | Stops and removes Compose containers and the project network. |
| `docker compose down -v` | Stops the stack and removes named volumes, including database data. |

