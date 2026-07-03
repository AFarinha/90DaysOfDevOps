# Tasks - Day 37

Use these commands as a practical checklist for revision. Replace placeholders such as `<image>` or `<container>` before running them.

## Commands

| Command | What it does |
|---|---|
| `docker run --rm hello-world` | Runs a test container from Docker Hub and removes it after it exits. |
| `docker run -d --name web -p 8080:80 nginx:alpine` | Starts an Nginx container in detached mode and maps host port 8080 to container port 80. |
| `docker ps` | Lists running containers. |
| `docker ps -a` | Lists all containers, including stopped containers. |
| `docker logs web` | Shows logs from the `web` container. |
| `docker exec -it web sh` | Opens an interactive shell inside the running `web` container. |
| `docker stop web` | Stops the running `web` container gracefully. |
| `docker rm web` | Removes the stopped `web` container. |
| `docker images` | Lists local Docker images and their sizes. |
| `docker image history nginx:alpine` | Shows the layer history for the `nginx:alpine` image. |
| `docker build -t demo-image:v1 .` | Builds an image from the current directory and tags it as `demo-image:v1`. |
| `docker tag demo-image:v1 <dockerhub-user>/demo-image:v1` | Creates a Docker Hub-ready tag for an existing local image. |
| `docker push <dockerhub-user>/demo-image:v1` | Pushes a tagged image to Docker Hub. |
| `docker volume create demo-data` | Creates a named Docker volume. |
| `docker volume ls` | Lists Docker volumes. |
| `docker volume inspect demo-data` | Shows details about the named volume. |
| `docker network create demo-net` | Creates a custom Docker bridge network. |
| `docker network ls` | Lists Docker networks. |
| `docker network inspect demo-net` | Shows network details, including connected containers. |
| `docker compose up -d` | Starts Compose services in detached mode. |
| `docker compose ps` | Shows the status of Compose services. |
| `docker compose logs -f` | Follows logs from all Compose services. |
| `docker compose down` | Stops and removes Compose containers and the default network. |
| `docker compose down -v` | Stops the stack and removes named volumes created by Compose. |
| `docker system df` | Shows Docker disk usage by images, containers, volumes and build cache. |
| `docker system prune` | Removes unused Docker resources after confirmation. |

