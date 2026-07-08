# Notes - Day 41

Summary: Learn GitHub Actions triggers and matrix builds.

- `pull_request` triggers workflows when pull requests are opened or updated.
- `schedule` uses cron syntax and runs in UTC.
- `workflow_dispatch` allows manual runs from the GitHub Actions UI.
- Matrix builds run the same job across multiple versions or operating systems.
- `exclude` removes unwanted matrix combinations.
- `fail-fast: false` lets the remaining matrix jobs continue even if one job fails.