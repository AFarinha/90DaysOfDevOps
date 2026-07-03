# Day 36 Task API

Small Flask API backed by Postgres, created for the Day 36 Docker project.

## Services

- `app`: Flask API served by Gunicorn.
- `db`: Postgres database.

## Run Locally with Compose

```bash
cp env.sample .env
docker compose up --build -d
curl http://localhost:8081/health
```

## API

Create a task:

```bash
curl -X POST http://localhost:8081/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Dockerize the app"}'
```

List tasks:

```bash
curl http://localhost:8081/tasks
```

## Environment Variables

| Variable | Purpose |
|---|---|
| `POSTGRES_DB` | Database name created by the Postgres container. |
| `POSTGRES_USER` | Database user. |
| `POSTGRES_PASSWORD` | Database password. |
| `DATABASE_HOST` | Hostname used by the app to reach Postgres. |
| `DATABASE_PORT` | Postgres port inside the Compose network. |

## Docker Hub Flow

After pushing the image to Docker Hub, run with:

```bash
APP_IMAGE=<dockerhub-user>/day36-task-api:v1 docker compose -f docker-compose.hub.yml up -d
```

