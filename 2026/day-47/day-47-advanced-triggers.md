# Day 47 - Advanced GitHub Actions Triggers

## Workflow Files

| Workflow | Trigger | Purpose |
|---|---|---|
| `.github/workflows/pr-lifecycle.yml` | Selected `pull_request` activity types | Reports PR lifecycle data and identifies merged PRs. |
| `.github/workflows/pr-checks.yml` | Pull requests targeting `main` | Checks changed file sizes, branch names, and PR descriptions. |
| `.github/workflows/scheduled-tasks.yml` | Two cron schedules and `workflow_dispatch` | Runs a GitHub API health check and reports the triggering schedule. |
| `.github/workflows/smart-triggers.yml` | Pushes to selected branches and application paths | Runs only for changes below `src/` or `app/`. |
| `.github/workflows/ignore-docs.yml` | Pushes to selected branches excluding documentation-only changes | Skips Markdown-only and `docs/`-only pushes. |
| `.github/workflows/tests.yml` | Every push and manual dispatch | Runs the existing Python test suite. |
| `.github/workflows/deploy-after-tests.yml` | Completion of `Run Tests` | Continues only after successful tests and warns on other conclusions. |
| `.github/workflows/external-trigger.yml` | `repository_dispatch` with `deploy-request` | Receives an environment from an external API request. |

All implementation YAML is stored in `2026/day-47/github-actions-practice/.github/workflows/`.

## Key Trigger Definitions

### Pull Request Lifecycle

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened, closed]
```

### Scheduled Tasks

```yaml
on:
  schedule:
    - cron: "30 2 * * 1"
    - cron: "0 */6 * * *"
  workflow_dispatch:
```

Additional requested cron expressions:

- Every weekday at 09:00 IST: `30 3 * * 1-5`
- First day of every month at midnight UTC: `0 0 1 * *`

### Application Paths

```yaml
on:
  push:
    branches: [main, "release/**"]
    paths:
      - "src/**"
      - "app/**"
```

### Documentation Exclusion

```yaml
on:
  push:
    branches: [main, "release/**"]
    paths-ignore:
      - "*.md"
      - "docs/**"
```

### Workflow Chaining

```yaml
on:
  workflow_run:
    workflows: ["Run Tests"]
    types: [completed]
```

The deployment job uses `if: github.event.workflow_run.conclusion == 'success'`. A separate warning job handles unsuccessful conclusions without deploying.

### External Dispatch

```yaml
on:
  repository_dispatch:
    types: [deploy-request]
```

## `workflow_run` Compared with `workflow_call`

`workflow_run` is event-driven. It starts a separate downstream workflow after another named workflow changes state, and the downstream run checks the upstream conclusion before continuing.

`workflow_call` is reuse-driven. A caller invokes another workflow as one of its jobs, passes a declared interface of inputs and secrets, and can consume declared outputs. It does not wait for an unrelated workflow run.

## Validation

The workflows require GitHub events for end-to-end validation. Use the commands in `tasks.md` to create the PR lifecycle events, manually test the schedule, send the external dispatch, and inspect the chained test and deploy runs.
