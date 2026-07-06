# Tasks - Day 39

Use these commands as a practical checklist for exploring CI/CD concepts. Replace placeholders such as `<repo-url>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-39` | Changes into the Day 39 directory before working on the notes. |
| `cat day-39-cicd-concepts.md` | Prints the CI/CD notes and pipeline diagram for review. |
| `git clone https://github.com/fastapi/fastapi.git open-source-repo` | Clones an open-source repository so you can inspect its CI/CD workflow files locally. |
| `find open-source-repo/.github/workflows -maxdepth 1 -type f -name "*.yml" -o -name "*.yaml"` | Lists GitHub Actions workflow files in the cloned repository. |
| `cat open-source-repo/.github/workflows/<workflow-file>.yml` | Prints one workflow file so you can identify triggers, jobs and steps. |
| `grep -n "on:" open-source-repo/.github/workflows/<workflow-file>.yml` | Finds the workflow trigger section. |
| `grep -n "jobs:" open-source-repo/.github/workflows/<workflow-file>.yml` | Finds the workflow jobs section. |
| `grep -n "runs-on:" open-source-repo/.github/workflows/<workflow-file>.yml` | Finds the runner definitions used by the workflow jobs. |

