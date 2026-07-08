# Tasks - Day 42

Use these commands as a practical checklist for the day. Replace placeholders such as `<runner-label>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-42` | Changes into the Day 42 directory before reviewing files. |
| `cat github-actions-practice/.github/workflows/hosted-runners.yml` | Prints the workflow that runs jobs on GitHub-hosted Ubuntu, Windows and macOS runners. |
| `cat github-actions-practice/.github/workflows/self-hosted.yml` | Prints the workflow that targets a self-hosted runner. |
| `git status` | Shows changed and untracked files before committing. |
| `git add notes.md tasks.md day-42-runners.md github-actions-practice/.github/workflows/hosted-runners.yml github-actions-practice/.github/workflows/self-hosted.yml` | Stages the Day 42 documentation and workflow files. |
| `git commit -m "Add day 42 runner workflows"` | Creates a commit for the Day 42 runner work. |
| `./run.sh` | Starts a configured self-hosted runner interactively in the terminal. |
| `sudo ./svc.sh install` | Installs the configured self-hosted runner as a background service on Linux. |
| `sudo ./svc.sh start` | Starts the self-hosted runner service after installation. |
| `sudo ./svc.sh status` | Checks whether the self-hosted runner service is running. |

