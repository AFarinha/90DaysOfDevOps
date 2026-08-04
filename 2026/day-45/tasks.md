# Tasks - Day 45

Use these commands as a practical checklist for the day. Replace placeholders such as `<branch-name>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-45/github-actions-practice` | Changes into the GitHub Actions practice repository for Day 45. |
| `cat Dockerfile` | Prints the Dockerfile used to build the container image. |
| `cat .dockerignore` | Prints the files excluded from the Docker build context. |
| `cat .github/workflows/docker-publish.yml` | Prints the workflow that builds and publishes the Docker image. |
| `cp env.sample .env` | Creates the local environment file used by Docker Compose. |
| `docker build -t day36-task-api:local .` | Builds the Day 36 Task API image locally and tags it as `day36-task-api:local`. |
| `docker compose up -d --build` | Builds the local image and starts the API plus Postgres in the background. |
| `curl http://localhost:8081/health` | Calls the API health endpoint to confirm the app can reach Postgres. |
| `curl -X POST http://localhost:8081/tasks -H "Content-Type: application/json" -d "{\"title\":\"learn docker cicd\"}"` | Creates a task through the API so the containerized app writes to Postgres. |
| `curl http://localhost:8081/tasks` | Lists tasks stored in Postgres through the API. |
| `docker compose down -v` | Stops the local stack and removes the named Postgres volume. |
| `git status` | Shows changed and untracked files before committing. |
| `git add README.md app.py Dockerfile .dockerignore docker-compose.yml docker-compose.hub.yml env.sample requirements.txt .github/workflows/docker-publish.yml` | Stages the Day 45 API, Docker, Compose and workflow files. |
| `git commit -m "Add Docker publish workflow"` | Creates a commit for the Day 45 Docker CI/CD workflow. |
| `git push` | Pushes the commit to GitHub so the workflow can run. |
| `gh run list --workflow docker-publish.yml` | Lists recent runs for the Docker publish workflow. |
| `docker pull afarinha/github-actions-practice:latest` | Pulls the latest pushed image from Docker Hub. |
| `APP_IMAGE=afarinha/github-actions-practice:latest docker compose -f docker-compose.hub.yml up -d` | Starts the Day 36 API using the image pushed to Docker Hub instead of building locally. |
| `APP_IMAGE=afarinha/github-actions-practice:latest docker compose -f docker-compose.hub.yml down -v` | Stops the Docker Hub based stack and removes the Postgres volume. |

## GitHub UI Setup

These steps are done in the GitHub web UI, not in the terminal.

| Step | What it does |
|---|---|
| `Settings -> Secrets and variables -> Actions -> New repository secret -> DOCKER_USERNAME` | Creates the Docker Hub username secret used by the workflow. |
| `Settings -> Secrets and variables -> Actions -> New repository secret -> DOCKER_TOKEN` | Creates the Docker Hub access token secret used by the workflow. |
| `Actions -> Docker Build and Push -> workflow run` | Opens the workflow run logs so you can confirm the image build and push. |
| `Docker Hub -> Repositories -> afarinha/github-actions-practice -> Tags` | Shows the pushed `latest` and `sha-<short-commit-hash>` image tags. |
