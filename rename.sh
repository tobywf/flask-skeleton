#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

old_name="flask_skeleton"
new_name=${1:-}
if [[ -z "$new_name" ]]; then
    echo "usage: $0 NAME"
    exit 1
fi

LC_ALL=C find "$old_name/" -type f -exec sed -i .bak "s/$old_name/$new_name/g" {} +
mv "$old_name/" "$new_name/"

# to undo the sed, move the folder back and run this:
# find flask_skeleton/ -type f -name '*.bak' -print0 | rename -0fx
