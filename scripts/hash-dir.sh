#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

for file in "$1"/*.jpg; do
    if [ -f "$file" ]; then
        md5sum "$file" | awk '{print $1}'
    fi
done
