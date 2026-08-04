# Day 46 Tasks - Reusable Workflows and Composite Actions

Run repository commands from `2026/day-46/github-actions-practice` unless a command says otherwise.

| Command | What it does |
|---|---|
| `git status` | Shows the current branch and all staged, modified, or untracked files before creating the Day 46 commit. |
| `git pull --ff-only` | Downloads remote changes and updates the current branch only when Git can perform a safe fast-forward without creating a merge commit. |
| `gh secret set DOCKER_TOKEN` | Securely prompts for a Docker Hub token and stores it as the `DOCKER_TOKEN` repository secret used by the caller workflow. |
| `git add .github/workflows/reusable-build.yml .github/workflows/call-build.yml .github/workflows/composite-action.yml .github/actions/setup-and-greet/action.yml` | Stages only the Day 46 reusable workflow, caller workflow, composite-action workflow, and custom action. |
| `git diff --cached` | Displays the exact staged changes so they can be reviewed before committing. |
| `git commit -m "Add reusable workflow and composite action"` | Creates a commit containing the staged Day 46 GitHub Actions files. |
| `git push origin main` | Pushes the commit to `main`, triggering the caller and composite-action workflows. |
| `gh run list --workflow call-build.yml` | Lists recent executions of the caller workflow and shows their status and run IDs. |
| `gh run list --workflow composite-action.yml` | Lists recent executions of the workflow that uses the custom composite action. |
| `gh run watch` | Watches an active workflow run until it finishes and reports whether its jobs succeeded. |
| `gh run view <RUN_ID> --log` | Prints the logs for a selected run so the reusable-workflow inputs, generated version, greeting, date, and runner OS can be verified. |
| `gh workflow run composite-action.yml` | Manually starts the composite-action workflow through its `workflow_dispatch` trigger. |
| `git rev-parse --short HEAD` | Prints the short commit SHA used in the generated build version. |

## Expected Results

The caller workflow should print `Building my-web-app for production`, confirm that the Docker token is set without exposing it, and return a value such as `v1.0-1a2b3c4`. The reporting job should print that same version. The composite action should print an English greeting, the UTC date, the runner OS, and `Composite action completed:true`.
