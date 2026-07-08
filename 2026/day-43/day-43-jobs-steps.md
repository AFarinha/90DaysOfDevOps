# Day 43 Jobs, Steps, Env Vars and Conditionals

## Multi-Job Workflow

File: `github-actions-practice/.github/workflows/multi-job.yml`

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Build app
        run: echo "Building the app"

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: echo "Running tests"

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy app
        run: echo "Deploying"
```

`needs:` creates a dependency between jobs. Here, `test` runs only after `build` succeeds, and `deploy` runs only after `test` succeeds.

## Environment Variables

File: `github-actions-practice/.github/workflows/env-vars.yml`

The workflow defines:

- workflow-level variable: `APP_NAME`
- job-level variable: `ENVIRONMENT`
- step-level variable: `VERSION`

It also prints GitHub context values:

- `${{ github.sha }}`
- `${{ github.actor }}`

## Job Outputs

File: `github-actions-practice/.github/workflows/job-outputs.yml`

One job writes a value to `$GITHUB_OUTPUT`, and another job reads it with:

```yaml
${{ needs.generate-date.outputs.today }}
```

Outputs are useful when one job produces data that another job needs, such as:

- image tags;
- version numbers;
- generated file paths;
- deployment targets;
- release metadata.

## Conditionals

File: `github-actions-practice/.github/workflows/conditionals.yml`

Examples included:

- run only on the `main` branch;
- run only if a previous step failed;
- run a job only for push events;
- use `continue-on-error: true`.

`continue-on-error: true` means the step may fail without failing the whole job. This is useful for optional checks or experiments that should not block the pipeline.

## Smart Pipeline

File: `github-actions-practice/.github/workflows/smart-pipeline.yml`

The smart pipeline:

- triggers on pushes to any branch;
- runs `lint` and `test` in parallel;
- runs `summary` after both finish;
- prints whether the push was to `main` or a feature branch;
- prints the commit message.

## What I Learned

- Jobs run in parallel by default unless `needs:` creates dependencies.
- Steps run in order inside a job.
- Outputs are the clean way to pass values between jobs.
- Conditionals make pipelines smarter by skipping work when it is not needed.

