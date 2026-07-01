### CRONTAB
1. Open and list
    crontab -e
2. Init cron job
    * * * * * cd /home/afarinha/git/90DaysOfDevOps/2023/day05 && ./2_backup.sh >> /home/afarinha/git/90DaysOfDevOps/2023/day05/backup.log 2>&1
3. Edit cron jobs
    crontab -r