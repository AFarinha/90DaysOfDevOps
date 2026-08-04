# Day 47 Tasks - Advanced GitHub Actions Triggers

Day 47 explicitly requires pull request lifecycle testing, so temporary branches are used in `github-actions-practice`. After the exercise PR is merged into `main`, run `cd ..` and commit the parent `90DaysOfDevOps` repository on `master`. For days that do not request a branch or pull request, commit directly to `main` instead.

## 1. Create the required pull request

| Command | What it does |
|---|---|
| `git status` | Shows the current branch and pending Day 47 workflow files. |
| `git switch main` | Switches `github-actions-practice` to `main` before creating the exercise branch. |
| `git pull --ff-only origin main` | Updates local `main` without creating a merge commit. |
| `git switch -c feature/day-47-triggers` | Creates the temporary feature branch explicitly required to test the pull request workflows. |
| `git add .github/workflows/pr-lifecycle.yml .github/workflows/pr-checks.yml .github/workflows/scheduled-tasks.yml .github/workflows/smart-triggers.yml .github/workflows/ignore-docs.yml .github/workflows/tests.yml .github/workflows/deploy-after-tests.yml .github/workflows/external-trigger.yml` | Stages only the eight workflow files created for Day 47. |
| `git diff --cached` | Displays the staged workflow changes for review before committing. |
| `git commit -m "Day 47 - Completed - Add advanced GitHub Actions triggers"` | Creates the Day 47 commit using the required message format. |
| `git push -u origin feature/day-47-triggers` | Publishes the feature branch and configures its upstream remote. |
| `gh pr create --base main --head feature/day-47-triggers --title "Day 47 - Advanced GitHub Actions triggers" --body "Adds PR lifecycle checks, schedules, path filters, workflow chaining, and an external trigger."` | Opens the pull request requested by the exercise with a non-empty description. |

## 2. Validate the pull request lifecycle

| Command | What it does |
|---|---|
| `gh pr checks --watch` | Watches the PR validation jobs and shows whether the file-size, branch-name, and body checks pass. |
| `git add <updated-file>` | Stages an intentional update made after opening the PR. Replace the placeholder with the actual workflow file changed. |
| `git commit -m "Day 47 - Completed - Update advanced GitHub Actions triggers"` | Commits the intentional PR update using the required message format. |
| `git push origin feature/day-47-triggers` | Pushes the update and triggers the PR `synchronize` event. |
| `gh pr merge --merge --delete-branch` | Merges the PR into `main`, triggers the `closed` and merged-only logic, and removes the remote feature branch. |
| `git switch main` | Returns the inner repository to `main` after the PR merge. |
| `git pull --ff-only origin main` | Updates local `main` with the merged Day 47 workflows. |

## 3. Validate the invalid branch-name check

Task 2 explicitly asks for a pull request from a badly named branch. Perform this separate negative test after the main Day 47 PR is merged.

| Command | What it does |
|---|---|
| `git switch -c day-47-invalid-name` | Creates a temporary branch that intentionally does not match `feature/*`, `fix/*`, or `docs/*`. |
| `git add <updated-file>` | Stages one intentional temporary change to an existing file so the test branch differs from `main`. |
| `git commit -m "Day 47 - Completed - Test invalid branch validation"` | Creates the negative-test commit using the required Day 47 message format. |
| `git push -u origin day-47-invalid-name` | Publishes the badly named branch so a PR can be opened. |
| `gh pr create --base main --head day-47-invalid-name --title "Day 47 - Test invalid branch name" --body "Verifies that the branch-name validation rejects an invalid branch."` | Opens the negative-test PR requested by Task 2. |
| `gh pr checks --watch` | Confirms that `branch-name-check` fails while the other applicable PR checks run. |
| `gh pr close day-47-invalid-name` | Closes the negative-test PR after the expected failure is confirmed. |
| `git switch main` | Returns to `main` after completing the negative test. |

## 4. Validate the remaining workflows

| Command | What it does |
|---|---|
| `gh workflow run scheduled-tasks.yml --ref main` | Manually starts the scheduled workflow from `main` through its `workflow_dispatch` trigger. |
| `gh run list --workflow scheduled-tasks.yml` | Lists recent manual and scheduled health-check runs. |
| `gh run list --workflow tests.yml` | Lists executions of the upstream `Run Tests` workflow. |
| `gh run list --workflow deploy-after-tests.yml` | Lists downstream runs triggered after the test workflow completes. |
| `gh api --method POST repos/AFarinha/github-actions-practice/dispatches -f event_type=deploy-request -F 'client_payload[environment]=production'` | Sends a `repository_dispatch` API request with event type `deploy-request` and a nested production environment payload. |
| `gh run list --workflow external-trigger.yml` | Confirms whether the external dispatch created a workflow run. |
| `gh run view <RUN_ID> --log` | Prints the logs of a selected run for trigger, condition, and payload verification. |

## 5. Commit `90DaysOfDevOps` on `master`

| Command | What it does |
|---|---|
| `cd ..` | Leaves `github-actions-practice` and returns to `2026/day-47` inside the parent repository. |
| `git branch --show-current` | Confirms that the parent `90DaysOfDevOps` repository is on `master`. |
| `git status` | Shows the Day 47 documentation and updated inner-repository reference. |
| `git add notes.md tasks.md day-47-advanced-triggers.md github-actions-practice` | Stages the Day 47 documentation and the merged `github-actions-practice` commit reference. |
| `git diff --cached --submodule=short` | Reviews the documentation and confirms the inner-repository commit that the parent will record. |
| `git commit -m "Day 47 - Completed - Add advanced GitHub Actions triggers"` | Creates the Day 47 commit in `90DaysOfDevOps` using the required message. |
| `git push origin master` | Pushes the parent repository commit to `master`. |

## Expected Sequence

1. Create `feature/day-47-triggers`, commit the workflows, and open the required PR to `main`.
2. Push an intentional update to trigger `synchronize`, then merge the PR to trigger `closed` and the merged-only step.
3. Create the explicitly requested invalid-name PR and confirm that `branch-name-check` fails.
4. Confirm that `Run Tests` completes before `Deploy After Tests` starts.
5. Manually run `scheduled-tasks.yml` and send the external dispatch request.
6. Run `cd ..` and commit the documentation plus the inner-repository reference to `master`.
