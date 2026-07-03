#!/bin/bash
read -p "Start countdown from: " NUMBER

while [ "$NUMBER" -ge 0 ]; do
    echo "$NUMBER"
    NUMBER=$((NUMBER - 1))
done

echo "Done!"

