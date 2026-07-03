#!/bin/bash
set -e

mkdir /tmp/devops-test || echo "Directory already exists"
cd /tmp/devops-test || { echo "Could not enter directory"; exit 1; }
touch created-by-safe-script.txt || { echo "Could not create file"; exit 1; }
echo "Created /tmp/devops-test/created-by-safe-script.txt"

