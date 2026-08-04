# Day 48 - GitHub Actions End-to-End CI/CD Project

## Project

The capstone reuses the Flask/Postgres Task API and multi-stage Dockerfile introduced on Day 36. A new endpoint test and five GitHub Actions workflows provide pull request validation, Docker publication, production deployment control, and scheduled runtime verification.

Docker Hub image: [afarinha/github-actions-practice](https://hub.docker.com/r/afarinha/github-actions-practice)

## Architecture

```text
PR opened or synchronized
  -> reusable-build-test.yml
  -> tests pass
  -> PR summary

Merge to main
  -> reusable-build-test.yml
  -> reusable-docker.yml
     -> afarinha/github-actions-practice:latest
     -> afarinha/github-actions-practice:sha-<short-sha>
  -> production environment
  -> deploy summary

Every 12 hours
  -> pull latest image
  -> PostgreSQL + Flask containers
  -> GET /health
  -> GitHub step summary
  -> cleanup
```

## Workflow Files

| File | Responsibility |
|---|---|
| `github-actions-practice/.github/workflows/reusable-build-test.yml` | Sets up Python and PostgreSQL, installs dependencies, runs tests, and returns the test result and short SHA. |
| `github-actions-practice/.github/workflows/reusable-docker.yml` | Logs in to Docker Hub, prepares multiple image tags, builds the Dockerfile, pushes the image, and returns its URL. |
| `github-actions-practice/.github/workflows/pr-pipeline.yml` | Calls only the build-test workflow for PRs targeting `main`; it never publishes Docker images. |
| `github-actions-practice/.github/workflows/main-pipeline.yml` | Runs tests, publishes `latest` and SHA tags, and enters the protected `production` environment. |
| `github-actions-practice/.github/workflows/health-check.yml` | Runs every 12 hours or manually, starts the database and app containers, checks `/health`, writes a summary, and cleans up. |

## Reusable Build and Test Interface

```yaml
inputs:
  python_version:
    type: string
    default: "3.12"
  run_tests:
    type: boolean
    default: true
outputs:
  test_result:
  short_sha:
```

## Reusable Docker Interface

```yaml
inputs:
  image_name:
    type: string
  tag:
    type: string
secrets:
  docker_username:
    required: true
  docker_token:
    required: true
outputs:
  image_url:
```

## Future Improvements

The next useful additions would be a staging environment, vulnerability scanning, deployment notifications, release tags, and an automated rollback that redeploys the previous successful image digest.

## Validation

Follow `tasks.md` to configure the two Docker Hub secrets and the `production` environment, open the required PR, merge it to `main`, inspect the full pipeline, and manually execute the scheduled health check. Screenshots are intentionally not part of this implementation.
