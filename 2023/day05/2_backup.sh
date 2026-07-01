#!/bin/bash

#chmod +x backup.sh
#./backup.sh

backup_dir="backups"
backup_file="work-backup-$(date +%Y%m%d_%H%M%S).tar.gz"

mkdir -p "$backup_dir"

tar --exclude="$backup_dir" -czf "$backup_dir/$backup_file" .

echo "Backup created successfully: $backup_dir/$backup_file"

#UNPACK
#mkdir restored-work
#tar -xzf backups/work-backup-20260701_143000.tar.gz -C restored-work