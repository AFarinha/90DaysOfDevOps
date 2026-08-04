# Notes - Day 45

Summary: Build and publish the Day 36 Task API Docker image automatically with GitHub Actions.

- The Day 36 Flask/Postgres Task API was reused as the application for this Docker CI/CD exercise.
- A Dockerfile was added to package the API as a container image.
- A Compose file was added to run the pushed Docker Hub image with Postgres.
- The workflow builds the image on every push to `main` and feature branches.
- Docker Hub login uses `DOCKER_USERNAME` and `DOCKER_TOKEN` repository secrets.
- The image is pushed only when the workflow runs on the `main` branch.
- Two tags are published: `latest` and `sha-<short-commit-hash>`.
- A status badge was added to the practice repository README.

## Git Push to Running Container Journey

1. A developer pushes code to GitHub.
2. GitHub Actions starts the `docker-publish.yml` workflow.
3. The runner checks out the repository.
4. The workflow builds the Docker image from the Dockerfile.
5. On `main`, the workflow logs in to Docker Hub using repository secrets.
6. The workflow pushes the image with `latest` and commit-based tags.
7. A user or server pulls the image from Docker Hub through Compose.
8. Docker runs the API container together with Postgres.

## Restart and Branch Behavior

- Pushes to feature branches should build the image but not push it.
- Pushes to `main` should build and push the image.
- The commit SHA tag makes it possible to run a specific build later.
