# Tasks - Day 42

Use these commands as a practical checklist for the day. Replace placeholders such as `<runner-label>` before running them.

## Repository commands

These commands are run inside this repository, in `2026/day-42` or in the nested `github-actions-practice` folder.

| Command | What it does |
|---|---|
| `cd 2026/day-42` | Changes into the Day 42 directory before reviewing files. |
| `cat github-actions-practice/.github/workflows/hosted-runners.yml` | Prints the workflow that runs jobs on GitHub-hosted Ubuntu, Windows and macOS runners. |
| `cat github-actions-practice/.github/workflows/self-hosted.yml` | Prints the workflow that targets a self-hosted runner. |
| `git status` | Shows changed and untracked files before committing. |
| `git add notes.md tasks.md day-42-runners.md github-actions-practice/.github/workflows/hosted-runners.yml github-actions-practice/.github/workflows/self-hosted.yml` | Stages the Day 42 documentation and workflow files so they can be committed. |
| `git commit -m "Add day 42 runner workflows"` | Creates a commit for the Day 42 runner work. |

## Self-hosted runner setup commands

These commands are not run inside this repository.

They are run inside the runner directory that GitHub tells you to create when you go to:

```text
GitHub repository -> Settings -> Actions -> Runners -> New self-hosted runner
```

GitHub will show commands to download a runner package, extract it, and configure it. After that setup, the runner directory contains files such as `config.sh`, `run.sh`, and `svc.sh`.

| Command | What it does |
|---|---|
| `./config.sh --url <repo-url> --token <runner-token>` | Registers the downloaded runner with your GitHub repository using the URL and token provided by GitHub. |
| `./run.sh` | Starts the configured self-hosted runner interactively in the terminal. This file exists only inside the downloaded runner directory. |
| `sudo ./svc.sh install` | Installs the configured self-hosted runner as a background service on Linux. This file exists only inside the downloaded runner directory. |
| `sudo ./svc.sh start` | Starts the self-hosted runner service after installation. |
| `sudo ./svc.sh status` | Checks whether the self-hosted runner service is running. |