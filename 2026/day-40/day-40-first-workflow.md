# Day 40 First Workflow

## Workflow YAML

Workflow file:

```text
github-actions-practice/.github/workflows/hello.yaml
```

```yaml
name: hello

on:
  push:

jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Print greeting
        run: echo "Hello from GitHub Actions!"

      - name: Print current date and time
        run: date

      - name: Print branch name
        run: |
          echo "Branch name: ${{ github.ref_name }}"

      - name: List repository files
        run: ls -la

      - name: Print runner operating system
        run: |
          echo "Runner OS: ${{ runner.os }}"
```

Note: the challenge says workflow files must end in `.yml`. GitHub Actions accepts both `.yml` and `.yaml`, but using `.yml` keeps the file aligned with the exercise instructions.

## Screenshot of the Green Run

Add the screenshot after pushing the workflow and confirming that the run is green in the GitHub Actions tab.

```text
Screenshot: <add-green-run-screenshot-here>
```

## Workflow Anatomy

### `on:`

`on:` defines what starts the workflow.

In this workflow:

```yaml
on:
  push:
```

The workflow runs every time code is pushed to the repository.

### `jobs:`

`jobs:` groups the work that GitHub Actions will run.

In this workflow:

```yaml
jobs:
  greet:
```

There is one job called `greet`.

### `runs-on:`

`runs-on:` chooses the runner machine that executes the job.

In this workflow:

```yaml
runs-on: ubuntu-latest
```

The job runs on a fresh Ubuntu runner managed by GitHub.

### `steps:`

`steps:` is the ordered list of actions or shell commands inside a job.

In this workflow, the steps:

- check out the repository;
- print a greeting;
- print the current date;
- print the branch name;
- list repository files;
- print the runner operating system.

### `uses:`

`uses:` runs a reusable GitHub Action.

In this workflow:

```yaml
uses: actions/checkout@v3
```

This downloads the repository code into the runner. Without checkout, the runner would not automatically have the repository files available.

### `run:`

`run:` executes shell commands directly on the runner.

Examples from this workflow:

```yaml
run: echo "Hello from GitHub Actions!"
```

```yaml
run: date
```

```yaml
run: ls -la
```

Use `run:` for normal terminal commands.

### `name:` on a step

Step `name:` gives a readable label to a workflow step.

Example:

```yaml
- name: Print greeting
  run: echo "Hello from GitHub Actions!"
```

This makes the Actions UI easier to read when checking what passed or failed.

## What I Learned

- Workflow files live under `.github/workflows/`.
- `on:` controls when the workflow starts.
- `jobs:` defines the work to run.
- `runs-on:` selects the runner environment.
- `steps:` run in order.
- `uses:` calls a reusable action.
- `run:` executes shell commands.
- Built-in variables such as `${{ github.ref_name }}` and `${{ runner.os }}` expose GitHub Actions context inside the workflow.

