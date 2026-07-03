#!/bin/bash
set -euo pipefail

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <log-directory> <source-directory> <backup-destination>"
    exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
log_file="/var/log/maintenance.log"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') $1" | tee -a "$log_file"
}

log "Starting maintenance"
"$script_dir/log_rotate.sh" "$1" 2>&1 | tee -a "$log_file"
"$script_dir/backup.sh" "$2" "$3" 2>&1 | tee -a "$log_file"
log "Maintenance finished"

