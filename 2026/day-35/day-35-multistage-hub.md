# Day 35 Multi-Stage Builds and Docker Hub

## App

The sample app is a small Go program in `go-hello/main.go`. It prints a message and is intentionally simple so the image-size difference is easy to focus on.

## Single-Stage Build

`Dockerfile.single` uses `golang:1.22-bookworm` as both build and runtime environment. This works, but the final image includes the Go compiler, build cache and OS packages that are not needed to run the compiled binary.

Build and inspect:

```bash
docker build -f Dockerfile.single -t day35-go-single:v1 .
docker images day35-go-single:v1
```

## Multi-Stage Build

`Dockerfile.multistage` uses:

- `golang:1.22-alpine` as the builder stage.
- `alpine:3.20` as the runtime stage.

Only the compiled binary is copied into the runtime image:

```dockerfile
COPY --from=builder /src/day35-app /usr/local/bin/day35-app
```

This makes the final image smaller because it does not include the compiler or source tree.

Build and inspect:

```bash
docker build -f Dockerfile.multistage -t day35-go-multistage:v1 .
docker images day35-go-multistage:v1
```

## Docker Hub Push

Tag the optimized image with your Docker Hub namespace:

```bash
docker tag day35-go-multistage:v1 <dockerhub-user>/day35-go-hello:v1
docker push <dockerhub-user>/day35-go-hello:v1
```

Docker Hub repository link:

```text
https://hub.docker.com/r/<dockerhub-user>/day35-go-hello
```

## Best Practices Applied

- Specific base image tags are used instead of `latest`.
- The final runtime image is based on Alpine.
- A non-root user runs the app in the final image.
- Build artifacts are copied from the builder stage instead of carrying the whole build environment.
- `.dockerignore` keeps local noise out of the build context.

## Size Comparison

Record your local results after building both images:

| Image | Size |
|---|---|
| `day35-go-single:v1` | `<record-size>` |
| `day35-go-multistage:v1` | `<record-size>` |

