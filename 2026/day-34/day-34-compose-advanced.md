# Day 34 Compose Advanced

## Stack

The exercise uses a three-service Compose stack:

- `web`: Flask app built from a local Dockerfile.
- `db`: Postgres database with a named volume and healthcheck.
- `redis`: Redis cache with a healthcheck.

## `depends_on` and Healthchecks

The web service depends on both Postgres and Redis using `condition: service_healthy`. This means the app waits for the services to pass their healthchecks instead of only waiting for containers to start.

## Restart Policies

- `restart: always`: useful for infrastructure services that should come back after crashes or daemon restarts.
- `restart: on-failure`: useful for jobs or services where only non-zero exits should trigger a restart.
- No restart policy: useful during debugging when failures should stay visible.

## Custom Dockerfile

The web service uses `build: ./app`, so Compose builds the image from `app/Dockerfile`. After changing app code, run:

```bash
docker compose up --build -d web
```

## Networks and Volumes

- `app_net`: explicit bridge network shared by all services.
- `postgres_data`: named volume for database persistence.

## Scaling Notes

`docker compose up -d --scale web=3` does not work cleanly with a fixed host port such as `8080:5000`, because multiple replicas cannot bind the same host port. In real setups, use a load balancer or reverse proxy and avoid fixed host port mappings per replica.

