#!/bin/bash

with_local() {
    local message="local value"
    echo "Inside function: $message"
}

without_local() {
    leaked_message="global value"
}

with_local
without_local
echo "Outside function: $leaked_message"

