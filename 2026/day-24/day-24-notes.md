# Day 24 Notes

## Merge

Fast-forward merge moves the target branch pointer when there is no divergence. Merge commits are created when branches diverged.

## Rebase

Rebase replays commits onto a new base. Do not rebase shared commits because it rewrites history.

## Squash

Squash merge combines multiple commits into one commit on the target branch.

## Stash

`git stash pop` applies and removes a stash. `git stash apply` applies but keeps it.

## Cherry Pick

Cherry-pick copies one commit onto the current branch. It can cause conflicts if the same lines changed.

