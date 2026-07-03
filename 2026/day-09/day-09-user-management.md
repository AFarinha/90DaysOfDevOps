# Day 09 Challenge

## Users and Groups Created

- Users: `tokyo`, `berlin`, `professor`, `nairobi`
- Groups: `developers`, `admins`, `project-team`

## Group Assignments

- `tokyo`: `developers`, `project-team`
- `berlin`: `developers`, `admins`
- `professor`: `admins`
- `nairobi`: `project-team`

## Directories Created

- `/opt/dev-project`: group `developers`, mode `775`
- `/opt/team-workspace`: group `project-team`, mode `775`

## Commands Used

Use the commands from `tasks.md` and paste relevant outputs or screenshots.

## What I Learned

- Groups are the clean way to share access between users.
- `usermod -aG` preserves existing group membership.
- Directory permissions must match the intended collaboration model.

