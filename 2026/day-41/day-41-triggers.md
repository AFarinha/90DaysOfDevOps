# Day 41 Triggers and Matrix Builds

## Pull Request and Scheduled Workflow

File: `github-actions-practice/.github/workflows/pr-check.yml`

```yaml
name: PR Check

on:
  pull_request:
    branches:
      - main
    types:
      - opened
      - synchronize
  schedule:
    - cron: "0 0 * * *"

jobs:
  pr-check:
    runs-on: ubuntu-latest
    steps:
      - name: Print pull request branch
        run: |
          echo "PR check running for branch: ${{ github.head_ref }}"

      - name: Print event name
        run: |
          echo "Triggered by: ${{ github.event_name }}"
```

This workflow runs when a pull request is opened or updated against `main`. It also runs every day at midnight UTC.

Cron answer for every Monday at 9 AM UTC:

```cron
0 9 * * 1
```

## Manual Workflow

File: `github-actions-practice/.github/workflows/manual.yml`

```yaml
name: Manual Deployment

on:
  workflow_dispatch:
    inputs:
      environment:
        description: "Target environment"
        required: true
        default: "staging"
        type: choice
        options:
          - staging
          - production

jobs:
  print-input:
    runs-on: ubuntu-latest
    steps:
      - name: Print selected environment
        run: |
          echo "Selected environment: ${{ inputs.environment }}"
```

This workflow is started manually from the Actions tab. The selected `environment` input is printed by the job.

## Matrix Workflow

File: `github-actions-practice/.github/workflows/matrix.yml`

```yaml
name: Matrix Build

on:
  push:
  workflow_dispatch:

jobs:
  python-version-check:
    strategy:
      fail-fast: false
      matrix:
        os:
          - ubuntu-latest
          - windows-latest
        python-version:
          - "3.10"
          - "3.11"
          - "3.12"
        exclude:
          - os: windows-latest
            python-version: "3.10"
    runs-on: ${{ matrix.os }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Print Python version
        run: python --version

      - name: Print matrix values
        run: echo "OS=${{ matrix.os }} Python=${{ matrix.python-version }}"
```

The matrix starts with 2 operating systems and 3 Python versions, which would normally create 6 jobs. One combination is excluded, so 5 jobs run.

`fail-fast: false` means that if one matrix job fails, the remaining jobs continue running. With the default `true`, GitHub cancels queued or in-progress matrix jobs when one fails.

## Screenshots

Add screenshots after running the workflows:

```text
PR workflow screenshot: <add-screenshot>
Manual workflow screenshot: <add-screenshot>
Matrix workflow screenshot: <add-screenshot>
```