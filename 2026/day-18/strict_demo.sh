#!/bin/bash
set -euo pipefail

echo "Strict mode enabled."
echo "Uncomment the next line to test set -u with an undefined variable."
# echo "$UNDEFINED_VARIABLE"
false | true

