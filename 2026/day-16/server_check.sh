#!/bin/bash
SERVICE_NAME="nginx"
read -p "Do you want to check the status? (y/n): " ANSWER

if [ "$ANSWER" = "y" ]; then
    if systemctl is-active --quiet "$SERVICE_NAME"; then
        echo "$SERVICE_NAME is active."
    else
        echo "$SERVICE_NAME is not active."
        systemctl status "$SERVICE_NAME" --no-pager
    fi
else
    echo "Skipped."
fi

