# Tasks - Day 35

Use these commands as a practical checklist for the day. Replace placeholders such as `<dockerhub-user>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-35/go-hello` | Changes into the Go app directory before building images. |
| `docker build -f Dockerfile.single -t day35-go-single:v1 .` | Builds the single-stage image that keeps the Go toolchain in the final image. |
| `docker images day35-go-single:v1` | Shows the local image size for the single-stage build. |
| `docker run --rm day35-go-single:v1` | Runs the single-stage container and prints the app output. |
| `docker build -f Dockerfile.multistage -t day35-go-multistage:v1 .` | Builds the optimized multi-stage image. |
| `docker images day35-go-multistage:v1` | Shows the local image size for the multi-stage build. |
| `docker run --rm day35-go-multistage:v1` | Runs the optimized container and prints the app output. |
| `docker login` | Authenticates the Docker CLI with Docker Hub. |
| `docker tag day35-go-multistage:v1 <dockerhub-user>/day35-go-hello:v1` | Creates a Docker Hub-ready tag for the optimized image. |
| `docker tag day35-go-multistage:v1 <dockerhub-user>/day35-go-hello:latest` | Adds a `latest` tag pointing to the same optimized image. |
| `docker push <dockerhub-user>/day35-go-hello:v1` | Pushes the versioned image tag to Docker Hub. |
| `docker push <dockerhub-user>/day35-go-hello:latest` | Pushes the `latest` image tag to Docker Hub. |
| `docker pull <dockerhub-user>/day35-go-hello:v1` | Pulls the specific versioned tag from Docker Hub to verify distribution. |
| `docker run --rm <dockerhub-user>/day35-go-hello:v1` | Runs the image pulled from Docker Hub. |

