# Day 48 Tasks - End-to-End GitHub Actions Pipeline

Day 48 explicitly requests a pull request, so a temporary branch is used in `github-actions-practice`. After merging it into `main`, commit the parent `90DaysOfDevOps` repository on `master`.

## 1. Configure GitHub prerequisites

Run these commands from `2026/day-48/github-actions-practice`.

| Command | What it does |
|---|---|
| `gh secret set DOCKER_USERNAME` | Securely prompts for the Docker Hub username and stores it as the repository secret used by the main pipeline. |
| `gh secret set DOCKER_TOKEN` | Securely prompts for a Docker Hub Personal Access Token and stores it without writing the value to the repository. |
| `gh api --method PUT repos/AFarinha/github-actions-practice/environments/production` | Creates the GitHub `production` environment if it does not already exist. Required reviewers must be configured separately in repository Settings under Environments. |

## 2. Create the required pull request

| Command | What it does |
|---|---|
| `git status` | Shows the current branch and pending Day 48 files before creating the exercise branch. |
| `git switch main` | Switches the inner repository to `main`. |
| `git pull --ff-only origin main` | Updates local `main` without creating a merge commit. |
| `git switch -c feature/day-48-capstone` | Creates the temporary branch required to test the PR-only pipeline. |
| `git add README.md tests/test_app.py .github/workflows/docker-publish.yml .github/workflows/reusable-build-test.yml .github/workflows/reusable-docker.yml .github/workflows/pr-pipeline.yml .github/workflows/main-pipeline.yml .github/workflows/health-check.yml` | Stages the Day 48 application test, README update, five pipeline workflows, and the manual-only trigger update for the legacy Docker workflow. |
| `git diff --cached` | Displays the exact staged changes before committing. |
| `git commit -m "Day 48 - Completed - Add end-to-end GitHub Actions pipeline"` | Creates the Day 48 commit using the required message format. |
| `git push -u origin feature/day-48-capstone` | Publishes the temporary feature branch and configures its upstream remote. |
| `gh pr create --base main --head feature/day-48-capstone --title "Day 48 - End-to-end GitHub Actions pipeline" --body "Adds reusable build, test, Docker publication, deployment, and scheduled health-check workflows."` | Opens the pull request required to test the PR pipeline. |
| `gh pr checks --watch` | Watches the PR pipeline and confirms that tests run without publishing a Docker image. |
| `gh pr merge --merge --delete-branch` | Merges the successful PR into `main` and removes the temporary remote branch. |
| `git switch main` | Returns the inner repository to `main` after the merge. |
| `git pull --ff-only origin main` | Updates local `main` with the merged capstone pipeline. |

## 3. Validate the main and health-check pipelines

| Command | What it does |
|---|---|
| `gh run list --workflow pr-pipeline.yml` | Lists PR-only runs so the test stage can be verified independently from Docker publication. |
| `gh run list --workflow main-pipeline.yml` | Lists full pipeline runs triggered after the PR reaches `main`. |
| `gh run view <RUN_ID> --log` | Prints a selected run's logs to verify the build-test, Docker, and deploy sequence. |
| `docker pull afarinha/github-actions-practice:latest` | Pulls the latest image published by the main pipeline from Docker Hub. |
| `gh workflow run health-check.yml --ref main` | Manually starts the scheduled health check without waiting for the 12-hour cron schedule. |
| `gh run list --workflow health-check.yml` | Lists manual and scheduled health-check executions. |

## 4. Commit `90DaysOfDevOps` on `master`

| Command | What it does |
|---|---|
| `cd ..` | Leaves `github-actions-practice` and returns to `2026/day-48` in the parent repository. |
| `git branch --show-current` | Confirms that the parent `90DaysOfDevOps` repository is on `master`. |
| `git status` | Shows the Day 48 documentation and updated inner-repository reference. |
| `git add notes.md tasks.md day-48-actions-project.md github-actions-practice` | Stages the Day 48 documentation and the merged `github-actions-practice` commit reference. |
| `git diff --cached --submodule=short` | Reviews the documentation and confirms the inner commit being recorded. |
| `git commit -m "Day 48 - Completed - Add end-to-end GitHub Actions pipeline"` | Creates the parent repository commit using the same required message. |
| `git push origin master` | Pushes the Day 48 parent commit to `master`. |
