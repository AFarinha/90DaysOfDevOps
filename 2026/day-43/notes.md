# Notes - Day 43

Summary: Learn how to control GitHub Actions workflow flow with jobs, steps, environment variables, outputs and conditionals.

- `needs:` creates job dependencies and controls execution order.
- Environment variables can be defined at workflow, job and step level.
- Job outputs pass values from one job to another.
- `if:` controls whether a job or step should run.
- `continue-on-error: true` allows a failing step to continue without failing the whole job.

