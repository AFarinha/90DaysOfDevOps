# Notes - Day 40

## Task 3: Workflow Anatomy

### `on:`

Defines what triggers the workflow.

Example:

```yaml
on:
  push:
    branches:
      - main
```

This means the workflow runs when code is pushed to the `main` branch.

Other common triggers:

```yaml
on:
  pull_request:
```

Runs when a pull request is opened or updated.

```yaml
on:
  workflow_dispatch:
```

Allows running the workflow manually from the GitHub Actions UI.

### `jobs:`

Defines the jobs that the workflow will run.

A workflow can have one job or many jobs.

Example:

```yaml
jobs:
  build:
```

Here, `build` is the name or id of a job. Inside it, we define where it runs and which steps it executes.

### `runs-on:`

Defines the runner machine where the job will execute.

Example:

```yaml
runs-on: ubuntu-latest
```

This means GitHub will run the job on a fresh Ubuntu virtual machine.

Common values:

```yaml
ubuntu-latest
windows-latest
macos-latest
```

For most CI pipelines, `ubuntu-latest` is common because it is fast and works well for Linux-based builds.

### `steps:`

Defines the list of actions or commands that run inside a job.

Example:

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4

  - name: Run tests
    run: pytest
```

Steps run in order. If one step fails, the job usually fails.

### `uses:`

Runs a reusable GitHub Action.

Example:

```yaml
uses: actions/checkout@v4
```

This uses the official `checkout` action to download the repository code into the runner.

Without this step, the runner starts empty and does not automatically have the source code available.

Another example:

```yaml
uses: actions/setup-python@v5
```

This installs and configures Python on the runner.

### `run:`

Runs a shell command directly on the runner.

Example:

```yaml
run: python --version
```

Or:

```yaml
run: pytest
```

Use `run:` when you want to execute normal terminal commands.

For multiple commands:

```yaml
run: |
  python -m pip install -r requirements.txt
  pytest
```

The `|` means this is a multi-line shell script.

### `name:` on a step

Gives a human-readable name to a step.

Example:

```yaml
- name: Run unit tests
  run: pytest
```

This name appears in the GitHub Actions UI, making the pipeline easier to read and debug.

Without `name:`, GitHub may show a less clear label based on the command or action.

## Simple Example

```yaml
name: Basic CI

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Show Python version
        run: python --version

      - name: Run tests
        run: pytest
```

Explanation:

- `name:` gives the workflow a display name.
- `on:` defines when the workflow runs.
- `jobs:` contains all jobs in the workflow.
- `test:` is one job.
- `runs-on:` chooses the runner machine.
- `steps:` lists what the job does.
- `uses:` runs a reusable GitHub Action.
- `run:` executes a shell command.
- Step `name:` makes each step readable in the GitHub Actions UI.

## Quick Summary

- `on:` decides when the workflow starts.
- `jobs:` groups the work the workflow performs.
- `runs-on:` chooses the machine.
- `steps:` run in order inside a job.
- `uses:` runs reusable GitHub Actions.
- `run:` executes shell commands.
- Step `name:` makes the workflow easier to read in the GitHub Actions UI.

