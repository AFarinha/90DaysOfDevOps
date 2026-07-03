# Day 19 Project

## Scripts

- `log_rotate.sh`: compresses old `.log` files and deletes old `.gz` archives.
- `backup.sh`: creates timestamped compressed backups.
- `maintenance.sh`: runs log rotation and backup with timestamped logging.

## Cron Entries

```cron
0 2 * * * /path/to/log_rotate.sh /var/log/myapp
0 3 * * 0 /path/to/backup.sh /srv/app /backups
*/5 * * * * /path/to/health_check.sh
0 1 * * * /path/to/maintenance.sh /var/log/myapp /srv/app /backups
```

## What I Learned

- Maintenance scripts should validate inputs.
- Cron should be documented before being applied.
- Backups need retention cleanup.

