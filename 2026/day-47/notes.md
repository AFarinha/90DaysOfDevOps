# Day 47 Notes - Advanced GitHub Actions Triggers

## Summary

Day 47 explored event-driven GitHub Actions pipelines. The exercises added pull request lifecycle events, PR quality gates, scheduled health checks, branch and path filters, workflow chaining, and external API triggers.

Event data is passed to shell commands through environment variables. This avoids placing pull request titles, descriptions, branch names, or external payloads directly inside shell scripts.

## Pull Request Events

The PR lifecycle workflow listens for `opened`, `synchronize`, `reopened`, and `closed`. The `synchronize` action occurs when new commits are pushed to the source branch of an open pull request. A closed pull request is only treated as merged when `github.event.pull_request.merged` is `true`.

The PR checks provide three independent results:

- `file-size-check` rejects changed files larger than 1 MB.
- `branch-name-check` accepts `feature/*`, `fix/*`, and `docs/*` branches.
- `pr-body-check` emits a warning for an empty description without failing the workflow.

## Cron Expressions

GitHub Actions schedules use POSIX cron expressions and UTC.

| Requirement | UTC cron expression | Explanation |
|---|---|---|
| Every Monday at 02:30 UTC | `30 2 * * 1` | Minute 30, hour 2, every month, Monday. |
| Every six hours | `0 */6 * * *` | Minute 0, every sixth hour. |
| Every weekday at 09:00 IST | `30 3 * * 1-5` | IST is UTC+05:30, so 09:00 IST is 03:30 UTC. |
| First day of every month at midnight UTC | `0 0 1 * *` | Minute 0, hour 0, day 1 of every month. |

Scheduled runs are not guaranteed to start at the exact minute. GitHub may delay them during periods of high Actions load, especially near the start of an hour, and sufficiently busy queues may drop jobs. Scheduled workflows only run from the default branch. In public repositories, GitHub automatically disables scheduled workflows after 60 days without repository activity; they must be re-enabled after activity resumes.

## Path Filters

Use `paths` when a workflow is relevant only to a known area, such as application code in `src/` or `app/`. Use `paths-ignore` when most changes should run the workflow but known non-functional changes, such as Markdown and `docs/`, should be skipped.

Branch and path filters are both evaluated. A push must match an allowed branch and an allowed path condition before the workflow starts.

## `workflow_run` and `workflow_call`

`workflow_run` reacts to the lifecycle of another workflow. The downstream workflow starts as a separate run after the named upstream workflow reaches the requested state, and it can inspect the upstream conclusion. It is useful for separating test and deployment pipelines.

`workflow_call` directly invokes a reusable workflow as a job in the caller. It passes declared inputs and secrets and can return outputs. It is useful for sharing implementation, not for reacting to an independently completed run.

## External Triggers

`repository_dispatch` allows a system outside GitHub to request a workflow through the GitHub API. Examples include a monitoring platform requesting rollback or recovery, a Slack bot starting an approved deployment, or a release service notifying GitHub that an artifact is ready. The workflow must validate and restrict external payloads before using them for real deployments.
