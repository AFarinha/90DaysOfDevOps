# Day 45 Docker Build and Push in GitHub Actions

## Workflow File

File: `github-actions-practice/.github/workflows/docker-publish.yml`

```yaml
name: Docker Build and Push

on:
  push:
    branches:
      - main
      - "feature/**"
  workflow_dispatch:

jobs:
  docker:
    name: Build and publish Docker image
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set image metadata
        id: vars
        run: |
          echo "short_sha=${GITHUB_SHA::7}" >> "$GITHUB_OUTPUT"

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Docker Hub
        if: github.ref == 'refs/heads/main'
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_TOKEN }}

      - name: Build and optionally push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: ./Dockerfile
          push: ${{ github.ref == 'refs/heads/main' }}
          tags: |
            ${{ secrets.DOCKER_USERNAME }}/github-actions-practice:latest
            ${{ secrets.DOCKER_USERNAME }}/github-actions-practice:sha-${{ steps.vars.outputs.short_sha }}
```

## Docker Hub Image

Image: `afarinha/github-actions-practice`

The image contains the Flask/Postgres Task API from Day 36.

Docker Hub link:

```text
https://hub.docker.com/r/afarinha/github-actions-practice
```

## What the Workflow Does

- `on:` starts the workflow on pushes to `main`, pushes to `feature/**` branches and manual runs.
- `jobs:` defines the work GitHub Actions should run.
- `runs-on:` selects a GitHub-hosted Ubuntu runner.
- `actions/checkout@v4` downloads the repository code into the runner.
- The metadata step creates a short commit SHA for the immutable image tag.
- `docker/setup-buildx-action@v3` enables Docker Buildx for the build.
- `docker/login-action@v3` logs in to Docker Hub, but only on `main`.
- `docker/build-push-action@v5` builds the image and pushes it only when the branch is `main`.

## Branch Behavior

Feature branch push:

- the workflow starts;
- the image is built;
- Docker Hub login is skipped;
- the image is not pushed.

Main branch push:

- the workflow starts;
- the image is built;
- Docker Hub login runs;
- `latest` and `sha-<short-commit-hash>` are pushed to Docker Hub.

## Pull and Run

```bash
docker pull afarinha/github-actions-practice:latest
cp env.sample .env
APP_IMAGE=afarinha/github-actions-practice:latest docker compose -f docker-compose.hub.yml up -d
curl http://localhost:8081/health
```

Expected output:

```text
{"status":"ok"}
```

## Full Journey

1. Code is pushed to GitHub.
2. GitHub Actions detects the push and starts the workflow.
3. The runner checks out the repository.
4. Docker builds an image using the Dockerfile.
5. If the branch is `main`, the workflow logs in to Docker Hub.
6. The image is pushed with `latest` and a commit-specific SHA tag.
7. Another machine pulls the image from Docker Hub.
8. Docker Compose starts the API container and a Postgres container.
9. The API connects to Postgres and serves requests on `http://localhost:8081`.

## Screenshots

Add screenshots after running the workflow:

```text
Green workflow run screenshot: <add-screenshot>
Docker Hub tags screenshot: <add-screenshot>
Container running locally screenshot: <add-screenshot>
```

## What I Learned

- CI/CD can build and publish Docker images without manual local pushes.
- Secrets keep Docker Hub credentials out of source control.
- Branch conditions prevent feature branches from publishing images.
- Commit SHA tags make image versions traceable to source code.
- Apps with runtime dependencies, such as databases, still need Compose or equivalent infrastructure when the pushed image is run.
