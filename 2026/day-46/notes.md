# Day 46 Notes - Reusable Workflows and Composite Actions

## Summary

Day 46 introduced two ways to reuse GitHub Actions automation. A reusable workflow centralizes complete jobs and is called from another workflow. A composite action packages multiple steps and is used as one step inside a job.

The practical work created a reusable build workflow with typed inputs, a required secret, and a build-version output. A caller passes values to that workflow and reports its output. A custom composite action prints a greeting, the current date, and the runner operating system before returning a `greeted` output.

## `workflow_call`

1. A reusable workflow is a workflow designed to be called by other workflows so common jobs do not have to be copied between repositories or pipelines.
2. `workflow_call` declares that a workflow can be invoked by another workflow. It also defines the inputs, secrets, and outputs that form the workflow's interface.
3. A reusable workflow is referenced at the job level and can contain one or more jobs. A regular or composite action is referenced inside a job step and contributes steps to that job.
4. A reusable workflow must be a YAML file directly inside `.github/workflows/`. It cannot be stored in a nested subdirectory of that directory.

## Reusable Workflow and Composite Action Comparison

| | Reusable Workflow | Composite Action |
|---|---|---|
| Triggered by | `workflow_call` and a job-level `uses:` | A step-level `uses:` |
| Can contain jobs? | Yes | No |
| Can contain multiple steps? | Yes, inside its jobs | Yes |
| Lives where? | `.github/workflows/<file>.yml` | Any repository directory containing `action.yml`; commonly `.github/actions/<name>/action.yml` |
| Can accept secrets directly? | Yes, through `workflow_call.secrets` | No dedicated secrets interface; the caller passes required values as inputs or environment variables |
| Best for | Reusing complete CI/CD jobs or pipelines | Reusing a sequence of steps within a job |

## Security Note

The reusable workflow only checks whether `DOCKER_TOKEN` is non-empty. It never prints the token value. The caller must store the token as a GitHub Actions repository secret named `DOCKER_TOKEN`.
