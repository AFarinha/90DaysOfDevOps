# Tasks - Day 43

Use these commands as a practical checklist for the day. Replace placeholders such as `<branch-name>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-43/github-actions-practice` | Changes into the GitHub Actions practice directory. |
| `cat .github/workflows/multi-job.yml` | Prints the workflow that demonstrates job dependencies with `needs:`. |
| `cat .github/workflows/env-vars.yml` | Prints the workflow that demonstrates workflow, job and step environment variables. |
| `cat .github/workflows/job-outputs.yml` | Prints the workflow that passes data between jobs with outputs. |
| `cat .github/workflows/conditionals.yml` | Prints the workflow that demonstrates step and job conditionals. |
| `cat .github/workflows/smart-pipeline.yml` | Prints the combined workflow with parallel jobs and a summary job. |
| `git status` | Shows changed and untracked files before committing. |
| `git add .github/workflows/multi-job.yml .github/workflows/env-vars.yml .github/workflows/job-outputs.yml .github/workflows/conditionals.yml .github/workflows/smart-pipeline.yml` | Stages all Day 43 workflow files. |
| `git commit -m "Add jobs steps env vars and conditionals workflows"` | Creates a commit with the Day 43 workflow examples. |
| `git push` | Pushes the workflow changes to GitHub so Actions can run them. |
| `gh run list` | Lists recent workflow runs so you can confirm that the new workflows triggered. |

