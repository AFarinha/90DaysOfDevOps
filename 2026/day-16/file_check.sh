#!/bin/bash
read -p "Enter a filename: " FILE_NAME

if [ -f "$FILE_NAME" ]; then
    echo "$FILE_NAME exists."
else
    echo "$FILE_NAME does not exist."
fi

