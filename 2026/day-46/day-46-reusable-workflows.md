# Day 46 - Reusable Workflows and Composite Actions

## Reusable Build Workflow

File: `.github/workflows/reusable-build.yml`

```yaml
name: Reusable Build

on:
  workflow_call:
    inputs:
      app_name:
        description: Application name shown in the build log
        required: true
        type: string
      environment:
        description: Target deployment environment
        required: true
        default: staging
        type: string
    secrets:
      docker_token:
        description: Docker Hub token passed by the caller
        required: true
    outputs:
      build_version:
        description: Version generated from the current commit SHA
        value: ${{ jobs.build.outputs.build_version }}

jobs:
  build:
    name: Build ${{ inputs.app_name }}
    runs-on: ubuntu-latest
    outputs:
      build_version: ${{ steps.version.outputs.build_version }}
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Display build target
        env:
          APP_NAME: ${{ inputs.app_name }}
          TARGET_ENVIRONMENT: ${{ inputs.environment }}
        run: echo "Building ${APP_NAME} for ${TARGET_ENVIRONMENT}"
      - name: Confirm Docker token
        env:
          DOCKER_TOKEN: ${{ secrets.docker_token }}
        run: |
          if [ -n "${DOCKER_TOKEN}" ]; then
            echo "Docker token is set: true"
          else
            echo "Docker token is set: false"
            exit 1
          fi
      - name: Generate build version
        id: version
        run: echo "build_version=v1.0-${GITHUB_SHA::7}" >> "${GITHUB_OUTPUT}"
```

## Caller Workflow

File: `.github/workflows/call-build.yml`

```yaml
name: Call Reusable Build

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    name: Run reusable build
    uses: ./.github/workflows/reusable-build.yml
    with:
      app_name: my-web-app
      environment: production
    secrets:
      docker_token: ${{ secrets.DOCKER_TOKEN }}

  report-version:
    name: Report build version
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Print build version
        env:
          BUILD_VERSION: ${{ needs.build.outputs.build_version }}
        run: echo "Reusable workflow returned ${BUILD_VERSION}"
```

## Composite Action

File: `.github/actions/setup-and-greet/action.yml`

```yaml
name: Setup and Greet
description: Prints a greeting and basic GitHub runner information

inputs:
  name:
    description: Name included in the greeting
    required: true
  language:
    description: Greeting language (en, pt, or es)
    required: false
    default: en

outputs:
  greeted:
    description: Indicates whether the greeting steps completed
    value: ${{ steps.result.outputs.greeted }}

runs:
  using: composite
  steps:
    - name: Print greeting
      shell: bash
      env:
        PERSON_NAME: ${{ inputs.name }}
        GREETING_LANGUAGE: ${{ inputs.language }}
      run: |
        case "${GREETING_LANGUAGE}" in
          en) greeting="Hello" ;;
          pt) greeting="Ola" ;;
          es) greeting="Hola" ;;
          *)
            echo "Unsupported language: ${GREETING_LANGUAGE}"
            exit 1
            ;;
        esac
        echo "${greeting}, ${PERSON_NAME}!"
    - name: Print runner information
      shell: bash
      run: |
        echo "Current date: $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
        echo "Runner OS: ${RUNNER_OS}"
    - name: Set action output
      id: result
      shell: bash
      run: echo "greeted=true" >> "${GITHUB_OUTPUT}"
```

The action is called from `.github/workflows/composite-action.yml` after `actions/checkout@v4` makes the local action available on the runner.

## Comparison

| | Reusable Workflow | Composite Action |
|---|---|---|
| Triggered by | `workflow_call` and a job-level `uses:` | A step-level `uses:` |
| Can contain jobs? | Yes | No |
| Can contain multiple steps? | Yes, inside its jobs | Yes |
| Lives where? | `.github/workflows/<file>.yml` | A directory containing `action.yml`, commonly below `.github/actions/` |
| Can accept secrets directly? | Yes, through `workflow_call.secrets` | No dedicated secrets interface; values must be passed by the caller |
| Best for | Complete jobs and CI/CD pipelines | Repeated steps within a job |

## Execution Evidence

The screenshot is pending the first successful run on GitHub because workflow execution requires a push to `main` and a configured `DOCKER_TOKEN` repository secret. After validation, store the screenshot inside `2026/day-46/screenshots/` and reference it here.

Expected caller output:

```text
Building my-web-app for production
Docker token is set: true
Reusable workflow returned v1.0-<short-sha>
```
