# Day 48 Notes - End-to-End GitHub Actions Pipeline

## Summary

Day 48 combined the GitHub Actions concepts from Days 40 through 47 into one CI/CD pipeline. The existing Flask/Postgres Task API from Day 36 is tested on pull requests, packaged as a Docker image after changes reach `main`, reported as ready for production deployment, and checked every 12 hours.

The pipeline uses reusable workflows to keep build, test, and Docker publication logic separate from event-specific caller workflows.

## Pipeline Architecture

```text
Pull request opened or updated
  -> reusable build and test
  -> PR summary
  -> no Docker publication

Pull request merged to main
  -> reusable build and test
  -> Docker build and push
     -> latest
     -> sha-<short-commit-sha>
  -> production environment
  -> deployment summary

Every 12 hours or manual dispatch
  -> pull latest image
  -> start PostgreSQL
  -> start application
  -> request /health
  -> write job summary
  -> remove containers and network
```

## Reusable Workflows

`reusable-build-test.yml` accepts a Python version and a boolean `run_tests` input. It starts PostgreSQL, installs application and test dependencies, runs the Python tests conditionally, and returns `test_result` plus a short commit SHA.

`reusable-docker.yml` accepts an image name and one or more tag values. It authenticates to Docker Hub, builds the repository Dockerfile, pushes every requested tag, and returns the first full image path as `image_url`.

## Pipeline Safety

The PR pipeline never calls the Docker publishing workflow, so pull requests cannot publish images. Docker credentials are passed only to the reusable Docker workflow through `DOCKER_USERNAME` and `DOCKER_TOKEN` repository secrets.

The previous `docker-publish.yml` workflow remains available through `workflow_dispatch`, but its automatic branch triggers are disabled to prevent duplicate Docker builds and pushes alongside the capstone pipeline.

The deployment job uses the GitHub `production` environment. Manual approval only occurs when the repository environment has a required-reviewer protection rule configured.

The application connects to PostgreSQL during startup and during `/health`. The test and scheduled health-check workflows therefore start a real PostgreSQL service instead of testing the Flask container in isolation.

## Next Improvements

- Add a staging environment before production.
- Send Slack or Teams notifications for failures and production approvals.
- Record the previous successful image tag and provide an automated rollback workflow.
- Add dependency and container vulnerability scanning.
- Publish deployment metadata and application version information.
