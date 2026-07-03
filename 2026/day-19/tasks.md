# Tasks - Day 19

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-19` | Changes into the target directory before running the exercise commands. |
| `chmod +x log_rotate.sh backup.sh maintenance.sh` | Changes file or directory permissions. |
| `mkdir -p /tmp/myapp-logs /tmp/backups /tmp/source-data` | Creates the requested directory path. |
| `echo "test log" > /tmp/myapp-logs/app.log` | Prints text, often redirected into a file or appended to one. |
| `echo "important data" > /tmp/source-data/data.txt` | Prints text, often redirected into a file or appended to one. |
| `./log_rotate.sh /tmp/myapp-logs` | Runs the log rotation script against the temporary log directory. |
| `./backup.sh /tmp/source-data /tmp/backups` | Creates a timestamped backup archive from the temporary source directory. |
| `sudo ./maintenance.sh /tmp/myapp-logs /tmp/source-data /tmp/backups` | Runs maintenance as root so it can write to /var/log/maintenance.log. |
| `crontab -l` | Lists or edits scheduled cron jobs for the current user. |
| `0 2 * * * /path/to/log_rotate.sh /var/log/myapp` | Schedules log rotation to run every day at 02:00. |
| `0 3 * * 0 /path/to/backup.sh /srv/app /backups` | Schedules the backup script to run every Sunday at 03:00. |
| `*/5 * * * * /path/to/health_check.sh` | Schedules a health check script to run every five minutes. |
| `0 1 * * * /path/to/maintenance.sh /var/log/myapp /srv/app /backups` | Schedules the combined maintenance script to run every day at 01:00. |
