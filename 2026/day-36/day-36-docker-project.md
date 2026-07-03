# Day 36 Docker Project

## App Chosen

I chose a small Python Flask task API with Postgres because it represents a common real-world pattern: a web service plus a persistent database.

The API supports:

- `GET /health`: checks database connectivity.
- `GET /tasks`: lists stored tasks.
- `POST /tasks`: creates a task.

## Dockerfile

The project Dockerfile is in `task-api/Dockerfile`.

Key decisions:

- `python:3.12-slim` keeps the image smaller than a full distribution image.
- The first stage builds Python wheels.
- The second stage installs only runtime dependencies.
- The app runs as a non-root `appuser`.
- `gunicorn` runs the Flask app in the container.

## Compose Setup

The Compose file defines:

- `app`: built from the Dockerfile.
- `db`: Postgres with a named volume.
- `task_api_net`: a custom bridge network.
- `postgres_data`: a named volume for database persistence.
- A Postgres healthcheck using `pg_isready`.
- `depends_on` with `condition: service_healthy` so the app waits for the database.

## Docker Hub

After building locally, tag and push the app image:

```bash
docker tag day36-task-api:local <dockerhub-user>/day36-task-api:v1
docker push <dockerhub-user>/day36-task-api:v1
```

Docker Hub repository link:

```text
https://hub.docker.com/r/<dockerhub-user>/day36-task-api
```

## Fresh Run Verification

Use `docker-compose.hub.yml` to test the pushed image:

```bash
APP_IMAGE=<dockerhub-user>/day36-task-api:v1 docker compose -f docker-compose.hub.yml up -d
curl http://localhost:8081/health
```

## Final Image Size

Record the result after building:

```text
day36-task-api:local = <record-size>
```

## Challenges and Fixes

- Database readiness is handled with a Postgres healthcheck.
- Configuration is moved to environment variables.
- `.dockerignore` keeps local files out of the build context.

