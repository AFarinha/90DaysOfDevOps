#!/bin/bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <log-directory>"
    exit 1
fi

log_dir="$1"

if [ ! -d "$log_dir" ]; then
    echo "Error: directory does not exist: $log_dir"
    exit 1
fi

compressed=$(find "$log_dir" -type f -name "*.log" -mtime +7 -print -exec gzip {} \; | wc -l)
deleted=$(find "$log_dir" -type f -name "*.gz" -mtime +30 -print -delete | wc -l)

echo "Compressed files: $compressed"
echo "Deleted archives: $deleted"

