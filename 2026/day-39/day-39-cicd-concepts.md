# Day 39 CI/CD Concepts

## The Problem

When five developers push code to the same repository and deploy manually, several things can go wrong:

- Changes may conflict because integration happens too late.
- Tests may be skipped or run differently by each developer.
- Manual deployment steps may be forgotten or performed in the wrong order.
- Production may receive code that was never tested in a clean environment.
- Rollbacks become harder because deployments are not repeatable.

`It works on my machine` means the code works only in one developer's local environment. This is a real problem because production has different dependencies, configuration, operating system settings, data and network conditions.

A team can deploy manually only a limited number of times safely. The more frequent the deployments, the more important automation becomes.

## CI vs CD vs CD

### Continuous Integration

Continuous Integration means developers integrate changes frequently into a shared branch. Every change should trigger automated checks such as linting, tests and builds.

Example: every pull request runs unit tests before it can be merged.

### Continuous Delivery

Continuous Delivery means the application is always kept in a deployable state. The pipeline builds, tests and packages the app, but a human usually approves the final production release.

Example: a successful merge creates a Docker image and prepares a staging deployment, then a release manager approves production.

### Continuous Deployment

Continuous Deployment means every change that passes the pipeline is automatically deployed to production without manual approval.

Example: a small SaaS team deploys every successful merge to production after automated tests, security checks and smoke tests pass.

## Pipeline Anatomy

| Part | What it does |
|---|---|
| Trigger | Starts the pipeline, for example a push, pull request, schedule or manual dispatch. |
| Stage | Groups related work, such as build, test, package or deploy. |
| Job | A unit of work inside a stage, usually executed on a runner. |
| Step | A single command or action inside a job. |
| Runner | The machine or container that executes the job. |
| Artifact | A file or package produced by a job, such as a test report, binary or Docker image metadata. |

## Pipeline Diagram

```text
Developer
  |
  | git push
  v
GitHub Repository
  |
  | trigger: push to main
  v
CI Pipeline
  |
  +--> Stage 1: Test
  |      - install dependencies
  |      - run unit tests
  |
  +--> Stage 2: Build
  |      - build Docker image
  |      - tag image with commit SHA
  |
  +--> Stage 3: Publish
  |      - push Docker image to registry
  |
  +--> Stage 4: Deploy to Staging
         - pull image on staging server
         - restart application
         - run smoke test
```

## Open-Source Workflow Review

Repository reviewed:

```text
<repo-name-or-url>
```

Workflow file:

```text
.github/workflows/<workflow-file>.yml
```

Findings:

- Trigger:
- Number of jobs:
- Runner:
- What it appears to do:

## What I Learned

- CI/CD is a practice for reducing integration and deployment risk.
- Pipelines make build, test and deploy steps repeatable.
- A failing pipeline is useful because it stops bad changes before they move further.

