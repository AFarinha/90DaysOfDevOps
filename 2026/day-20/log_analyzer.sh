#!/bin/bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <log-file>"
    exit 1
fi

log_file="$1"

if [ ! -f "$log_file" ]; then
    echo "Error: file does not exist: $log_file"
    exit 1
fi

report_file="log_report_$(date +%Y-%m-%d).txt"
total_lines=$(wc -l < "$log_file")
error_count=$(grep -Ec "ERROR|Failed" "$log_file" || true)

echo "Total error count: $error_count"
echo "--- Critical Events ---"
grep -n "CRITICAL" "$log_file" | sed 's/^/Line /' || true

{
    echo "Date of analysis: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "Log file: $log_file"
    echo "Total lines processed: $total_lines"
    echo "Total error count: $error_count"
    echo
    echo "--- Top 5 Error Messages ---"
    grep "ERROR" "$log_file" \
        | sed -E 's/^.*ERROR[] ]*//' \
        | sort \
        | uniq -c \
        | sort -rn \
        | head -5 \
        || true
    echo
    echo "--- Critical Events ---"
    grep -n "CRITICAL" "$log_file" | sed 's/^/Line /' || true
} > "$report_file"

echo "Report generated: $report_file"

