# Tasks - Day 36

Use these commands as a practical checklist for the day. Replace placeholders such as `<dockerhub-user>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-36/task-api` | Changes into the Dockerized project directory. |
| `cp env.sample .env` | Creates the local environment file used by Docker Compose. |
| `docker compose config` | Validates and renders the Compose configuration after variable interpolation. |
| `docker compose up --build -d` | Builds the Flask app image and starts the app plus Postgres in detached mode. |
| `docker compose ps` | Shows container state and database health status. |
| `docker compose logs -f app` | Follows application logs to confirm the API started correctly. |
| `curl http://localhost:8081/health` | Checks whether the API can reach Postgres successfully. |
| `curl -X POST http://localhost:8081/tasks -H "Content-Type: application/json" -d "{\"title\":\"Dockerize the app\"}"` | Creates a task through the API. |
| `curl http://localhost:8081/tasks` | Lists tasks stored in Postgres. |
| `docker images day36-task-api:local` | Shows the locally built app image size. |
| `docker tag day36-task-api:local <dockerhub-user>/day36-task-api:v1` | Creates a Docker Hub-ready tag for the app image. |
| `docker push <dockerhub-user>/day36-task-api:v1` | Pushes the app image to Docker Hub. |
| `APP_IMAGE=<dockerhub-user>/day36-task-api:v1 docker compose -f docker-compose.hub.yml up -d` | Runs the stack using the pushed image instead of building locally. |
| `docker compose down` | Stops and removes the local Compose stack containers and network. |
| `docker compose down -v` | Stops the stack and removes the Postgres data volume. |

