# Tasks - Day 29

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `docker --version` | Checks the installed Docker version. |
| `docker run hello-world` | Creates and starts a container from the specified image. |
| `docker run -d --name web -p 8080:80 nginx` | Creates and starts a container from the specified image. |
| `docker ps` | Lists running containers or all containers when -a is used. |
| `curl -I http://localhost:8080` | Makes an HTTP request or checks HTTP headers for the target URL. |
| `docker run -it --name ubuntu-lab ubuntu bash` | Creates and starts a container from the specified image. |
| `docker ps -a` | Lists running containers or all containers when -a is used. |
| `docker logs web` | Shows logs produced by a container. |
| `docker exec web nginx -v` | Runs a command inside an existing container. |
| `docker stop web` | Stops a running container gracefully. |
| `docker rm web` | Removes a stopped container. |
