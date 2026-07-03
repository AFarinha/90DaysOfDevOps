# Day 37 Revision

## Self-Assessment

| Topic | Status |
|---|---|
| Run containers from Docker Hub | Can do |
| List, stop and remove containers/images | Can do |
| Explain image layers and caching | Shaky |
| Write a Dockerfile from scratch | Can do |
| Explain CMD vs ENTRYPOINT | Shaky |
| Build and tag custom images | Can do |
| Create and use named volumes | Can do |
| Use bind mounts | Can do |
| Create custom networks | Can do |
| Write Docker Compose files | Can do |
| Use `.env` files in Compose | Can do |
| Write a multi-stage Dockerfile | Can do |
| Push an image to Docker Hub | Can do |
| Use healthchecks and `depends_on` | Can do |

## Quick-Fire Answers

1. An image is a read-only template; a container is a running instance of an image.
2. Data inside a removed container is lost unless it is stored in a volume or bind mount.
3. Containers on the same custom network can communicate by service/container name through Docker DNS.
4. `docker compose down -v` removes named volumes in addition to containers and networks.
5. Multi-stage builds keep compilers and build tools out of the final runtime image.
6. `COPY` copies files from the build context; `ADD` can also unpack archives and fetch remote URLs, so `COPY` is usually clearer.
7. `-p 8080:80` maps host port `8080` to container port `80`.
8. Use `docker system df` to check Docker disk usage.

## Weak Spots to Revisit

### Image Layers and Caching

Redo Day 30 image history checks:

```bash
docker image history nginx:alpine
docker build -t cache-demo:v1 .
docker build -t cache-demo:v2 .
```

### CMD vs ENTRYPOINT

Redo Day 31 command override checks:

```bash
docker run --rm cmd-demo:v1
docker run --rm cmd-demo:v1 echo custom command
docker run --rm entrypoint-demo:v1 hello
```

