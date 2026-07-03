# Day 25 Notes

## Reset vs Revert

| | `git reset` | `git revert` |
|---|---|---|
| What it does | Moves branch pointer | Creates an inverse commit |
| Removes commit from history? | Can remove from branch history | No |
| Safe for shared branches? | Usually no | Yes |
| When to use | Local cleanup | Undo public/shared changes |

## Branching Strategies

- GitFlow: `main`, `develop`, feature, release and hotfix branches.
- GitHub Flow: short-lived branches merged to `main`.
- Trunk-Based Development: very short branches or direct commits to trunk with strong CI.

For a small team shipping weekly, GitHub Flow is usually enough. For scheduled enterprise releases, GitFlow can fit better.

