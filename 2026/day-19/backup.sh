#!/bin/bash
set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <source-directory> <backup-destination>"
    exit 1
fi

source_dir="$1"
backup_dest="$2"

if [ ! -d "$source_dir" ]; then
    echo "Error: source directory does not exist: $source_dir"
    exit 1
fi

mkdir -p "$backup_dest"
timestamp=$(date +%Y-%m-%d)
archive="$backup_dest/backup-$timestamp.tar.gz"

tar -czf "$archive" "$source_dir"

if [ -f "$archive" ]; then
    echo "Archive created: $archive"
    du -h "$archive"
else
    echo "Error: archive was not created"
    exit 1
fi

find "$backup_dest" -type f -name "backup-*.tar.gz" -mtime +14 -delete

