# Tasks - Day 41

Use these commands as a practical checklist for the day. Replace placeholders such as `<branch-name>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-41/github-actions-practice` | Changes into the GitHub Actions practice repository. |
| `cat .github/workflows/pr-check.yml` | Prints the pull request and scheduled workflow file for review. |
| `cat .github/workflows/manual.yml` | Prints the manually triggered workflow file for review. |
| `cat .github/workflows/matrix.yml` | Prints the matrix workflow file for review. |
| `git switch -c <branch-name>` | Creates and switches to a new branch for testing the pull request trigger. |
| `git status` | Shows changed and untracked files in the practice repository. |
| `git add .github/workflows/pr-check.yml .github/workflows/manual.yml .github/workflows/matrix.yml` | Stages the workflow files for commit. |
| `git commit -m "Add trigger and matrix workflows"` | Creates a commit containing the workflow changes. |
| `git push -u origin <branch-name>` | Pushes the branch to GitHub and sets the upstream branch. |
| `gh pr create --fill` | Creates a pull request from the pushed branch using GitHub CLI. |
| `gh workflow list` | Lists workflows available in the repository. |
| `gh run list` | Lists recent workflow runs so you can inspect trigger results. |