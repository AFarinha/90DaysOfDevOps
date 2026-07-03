# Tasks - Day 30

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `docker pull nginx` | Downloads an image from a registry. |
| `docker pull ubuntu` | Downloads an image from a registry. |
| `docker pull alpine` | Downloads an image from a registry. |
| `docker images` | Lists local Docker images. |
| `docker image history nginx` | Shows the layer history of a Docker image. |
| `docker inspect nginx` | Shows detailed JSON metadata for an image, container, network or volume. |
| `docker create --name lifecycle-nginx nginx` | Creates a container without starting it. |
| `docker start lifecycle-nginx` | Starts an existing stopped or created container. |
| `docker pause lifecycle-nginx` | Pauses processes inside a running container. |
| `docker unpause lifecycle-nginx` | Resumes a paused container. |
| `docker stop lifecycle-nginx` | Stops a running container gracefully. |
| `docker restart lifecycle-nginx` | Stops and starts a container again. |
| `docker kill lifecycle-nginx` | Forcefully stops a running container. |
| `docker rm lifecycle-nginx` | Removes a stopped container. |
| `docker run -d --name nginx-live -p 8080:80 nginx` | Creates and starts a container from the specified image. |
| `docker logs nginx-live` | Shows logs produced by a container. |
| `docker exec -it nginx-live sh` | Runs a command inside an existing container. |
| `docker inspect nginx-live` | Shows detailed JSON metadata for an image, container, network or volume. |
| `docker system df` | Shows Docker disk usage. |
| `docker system prune` | Removes unused Docker resources after confirmation. |
