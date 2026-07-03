#!/bin/bash
set -euo pipefail

print_header() {
    echo
    echo "== $1 =="
}

host_info() {
    print_header "Host and OS"
    hostname
    cat /etc/os-release | head -5
}

uptime_info() {
    print_header "Uptime"
    uptime
}

disk_usage() {
    print_header "Disk Usage"
    df -h | head
}

memory_usage() {
    print_header "Memory Usage"
    free -h
}

top_processes() {
    print_header "Top CPU Processes"
    ps aux --sort=-%cpu | head -6
}

main() {
    host_info
    uptime_info
    disk_usage
    memory_usage
    top_processes
}

main

