# Tasks - Day 24

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `git switch main` | Switches to another branch or creates and switches to a new branch. |
| `git switch -c feature-login` | Switches to another branch or creates and switches to a new branch. |
| `git commit --allow-empty -m "Add login step one"` | Creates a commit from staged changes with the provided message. |
| `git commit --allow-empty -m "Add login step two"` | Creates a commit from staged changes with the provided message. |
| `git switch main` | Switches to another branch or creates and switches to a new branch. |
| `git merge feature-login` | Integrates another branch into the current branch. |
| `git switch -c feature-dashboard` | Switches to another branch or creates and switches to a new branch. |
| `git commit --allow-empty -m "Add dashboard step"` | Creates a commit from staged changes with the provided message. |
| `git switch main` | Switches to another branch or creates and switches to a new branch. |
| `git commit --allow-empty -m "Main branch update"` | Creates a commit from staged changes with the provided message. |
| `git switch feature-dashboard` | Switches to another branch or creates and switches to a new branch. |
| `git rebase main` | Replays current branch commits on top of another base commit. |
| `git stash push -m "work in progress"` | Stores or restores uncommitted work temporarily. |
| `git stash list` | Stores or restores uncommitted work temporarily. |
| `git stash pop` | Stores or restores uncommitted work temporarily. |
| `git cherry-pick <commit-hash>` | Applies a specific commit onto the current branch. |
| `git log --oneline --graph --all` | Displays commit history, often in a compact or graph view. |
