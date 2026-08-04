# Day 49 Tasks - DevSecOps

## Prepare the Pull Request

The Day 49 dependency review requires a pull request event, so this exercise intentionally uses a feature branch.

| Command | What it does |
| --- | --- |
| <code>cd ~/git/90DaysOfDevOps/2026/day-49/github-actions-practice</code> | Enters the application repository used for the Day 49 security changes. |
| <code>git switch main</code> | Selects the inner repository's main branch before creating the exercise branch. |
| <code>git pull --ff-only origin main</code> | Downloads the latest main branch without creating a merge commit. |
| <code>git switch -c feature/day-49-devsecops</code> | Creates the branch required to test the pull request security pipeline. |
| <code>git diff --check</code> | Checks the changes for whitespace errors before committing. |
| <code>git add .github/workflows/main-pipeline.yml .github/workflows/pr-pipeline.yml .github/workflows/reusable-docker.yml</code> | Stages only the Day 49 workflow changes. |
| <code>git commit -m "Day 49 - Completed - Add DevSecOps security checks"</code> | Creates the inner repository commit using the agreed message format. |
| <code>git push -u origin feature/day-49-devsecops</code> | Publishes the exercise branch and configures its upstream branch. |
| <code>gh pr create --base main --head feature/day-49-devsecops --title "Day 49 - Add DevSecOps security checks" --body "Adds dependency review, Trivy image scanning, and least-privilege workflow permissions."</code> | Opens the pull request that triggers dependency review and the PR test pipeline. |

## Validate the PR Pipeline

| Command | What it does |
| --- | --- |
| <code>gh pr checks</code> | Shows the checks attached to the current pull request, including dependency review. |
| <code>gh run list --workflow "PR Pipeline" --limit 5</code> | Lists recent PR pipeline runs and their IDs. |
| <code>gh run watch RUN_ID</code> | Follows a selected workflow run; replace RUN_ID with the listed ID. |
| <code>gh run view RUN_ID --log</code> | Prints the complete log for a selected run. |
| <code>gh pr merge --merge --delete-branch</code> | Merges the approved pull request into main and removes the remote feature branch. |
| <code>git switch main</code> | Returns the inner repository to main after the merge. |
| <code>git pull --ff-only origin main</code> | Updates the local main branch with the merged security changes. |

## Enable GitHub Secret Protection

In the GitHub repository, open Settings, then Security or Code security, and open Advanced Security. Enable secret scanning and repository push protection when those controls are available. Do not commit a real or example credential to test the feature.

## Validate the Main Pipeline

| Command | What it does |
| --- | --- |
| <code>gh run list --workflow "Main Pipeline" --limit 5</code> | Lists recent main pipeline runs after the pull request is merged. |
| <code>gh run watch RUN_ID</code> | Waits for the selected main pipeline run to finish. |
| <code>gh run view RUN_ID --log</code> | Displays the Trivy table and the remaining build, push, and deployment logs. |

If Trivy reports a CRITICAL or HIGH vulnerability, the workflow must fail before the Docker Hub login and push steps. Review the affected package and fixed version before changing the severity policy.

## Commit the Parent Repository

Run these commands only after the inner repository changes are committed, pushed, and merged.

| Command | What it does |
| --- | --- |
| <code>cd ..</code> | Leaves the inner repository and returns to the Day 49 folder in the parent repository. |
| <code>git switch master</code> | Selects the parent 90DaysOfDevOps repository's master branch. |
| <code>git add notes.md tasks.md day-49-devsecops.md github-actions-practice</code> | Stages the Day 49 documentation and the updated inner repository reference. |
| <code>git commit -m "Day 49 - Completed - Add DevSecOps security checks"</code> | Creates the parent repository commit using the same Day 49 message. |
| <code>git push origin master</code> | Publishes the Day 49 documentation and inner repository reference. |
