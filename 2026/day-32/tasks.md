# Tasks - Day 32

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `docker volume create pgdata` | Creates a named Docker volume. |
| `docker run -d --name pg1 -e POSTGRES_PASSWORD=devops -v pgdata:/var/lib/postgresql/data postgres:16-alpine` | Creates and starts a container from the specified image. |
| `docker volume ls` | Lists Docker volumes. |
| `docker volume inspect pgdata` | Shows detailed metadata for a Docker volume. |
| `docker stop pg1` | Stops a running container gracefully. |
| `docker rm pg1` | Removes a stopped container. |
| `docker run -d --name pg2 -e POSTGRES_PASSWORD=devops -v pgdata:/var/lib/postgresql/data postgres:16-alpine` | Creates and starts a container from the specified image. |
| `cd 2026/day-32/bind-mount-site` | Changes into the target directory before running the exercise commands. |
| `docker run -d --name bind-nginx -p 8080:80 -v "$PWD":/usr/share/nginx/html:ro nginx:alpine` | Creates and starts a container from the specified image. |
| `curl -I http://localhost:8080` | Makes an HTTP request or checks HTTP headers for the target URL. |
| `docker network ls` | Lists Docker networks. |
| `docker network inspect bridge` | Shows detailed metadata for a Docker network. |
| `docker network create my-app-net` | Creates a custom Docker network. |
| `docker run -d --name app-db --network my-app-net -e POSTGRES_PASSWORD=devops -v pgdata:/var/lib/postgresql/data postgres:16-alpine` | Creates and starts a container from the specified image. |
| `docker run --rm --network my-app-net alpine sh -c "apk add --no-cache postgresql-client && nc -zv app-db 5432"` | Creates and starts a container from the specified image. |
