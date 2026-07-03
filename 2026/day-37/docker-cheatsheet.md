# Docker Cheat Sheet

## Container Commands

| Command | Use |
|---|---|
| `docker run <image>` | Create and start a container from an image. |
| `docker run -it <image> sh` | Start an interactive shell in a new container. |
| `docker run -d --name <name> <image>` | Run a container in detached mode with a name. |
| `docker ps` | List running containers. |
| `docker ps -a` | List all containers. |
| `docker stop <container>` | Stop a running container. |
| `docker rm <container>` | Remove a stopped container. |
| `docker exec -it <container> sh` | Run a shell inside a running container. |
| `docker logs <container>` | Show container logs. |

## Image Commands

| Command | Use |
|---|---|
| `docker images` | List local images. |
| `docker pull <image>` | Download an image from a registry. |
| `docker build -t <name>:<tag> .` | Build an image from a Dockerfile. |
| `docker tag <local> <user>/<repo>:<tag>` | Add a registry-ready tag to an image. |
| `docker push <user>/<repo>:<tag>` | Push an image to Docker Hub. |
| `docker rmi <image>` | Remove a local image. |
| `docker image history <image>` | Show image layers. |

## Volume Commands

| Command | Use |
|---|---|
| `docker volume create <name>` | Create a named volume. |
| `docker volume ls` | List volumes. |
| `docker volume inspect <name>` | Show volume metadata and mountpoint. |
| `docker volume rm <name>` | Remove an unused volume. |

## Network Commands

| Command | Use |
|---|---|
| `docker network create <name>` | Create a custom network. |
| `docker network ls` | List networks. |
| `docker network inspect <name>` | Show network configuration and connected containers. |
| `docker network connect <network> <container>` | Attach a container to a network. |

## Compose Commands

| Command | Use |
|---|---|
| `docker compose up -d` | Start services in detached mode. |
| `docker compose up --build -d` | Rebuild images and start services. |
| `docker compose ps` | Show Compose service status. |
| `docker compose logs -f` | Follow logs for all services. |
| `docker compose logs <service>` | Show logs for one service. |
| `docker compose down` | Stop and remove containers and network. |
| `docker compose down -v` | Also remove named volumes created by the project. |

## Cleanup Commands

| Command | Use |
|---|---|
| `docker system df` | Show Docker disk usage. |
| `docker system prune` | Remove unused containers, networks, images and build cache. |
| `docker volume prune` | Remove unused volumes. |
| `docker image prune` | Remove dangling images. |

## Dockerfile Instructions

| Instruction | Use |
|---|---|
| `FROM` | Select the base image. |
| `RUN` | Execute commands during image build. |
| `COPY` | Copy files from build context into the image. |
| `WORKDIR` | Set the working directory. |
| `EXPOSE` | Document the port the app listens on. |
| `CMD` | Set the default command. |
| `ENTRYPOINT` | Set the main executable for the container. |

