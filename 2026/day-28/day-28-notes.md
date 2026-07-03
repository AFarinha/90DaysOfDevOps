# Day 28 Notes

## Weak Spots to Revisit

1.
2.
3.

## Quick-Fire Answers

1. `chmod 755 script.sh` gives owner rwx, group rx and others rx.
2. A process is a running program; a service is a managed background process.
3. Use `ss -tulpn | grep :8080`.
4. `set -euo pipefail` exits on errors, unset variables and failed pipeline parts.
5. `reset --hard` rewrites local history and discards changes; `revert` creates a new undo commit.
6. GitHub Flow for a small team shipping weekly.
7. `git stash` saves temporary uncommitted work.
8. Cron: `0 3 * * * /path/to/script.sh`.
9. `fetch` downloads; `pull` downloads and integrates.
10. LVM provides flexible logical volumes over physical storage.

## Teach It Back

Git branches are separate lines of work. You create a branch to make changes without affecting `main`. When the work is ready, you merge it back. This keeps experiments, features and fixes isolated until they are reviewed.

