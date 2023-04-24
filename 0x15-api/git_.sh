#!/bin/bash

# Check if a commit message is provided as an argument
if [ -z "$1" ]; then
  echo "Please provide a commit message as an argument."
  exit 1
fi

# Add all changes to the staging area
git add .

# Commit changes with the provided commit message
git commit -m "$1"

# Push changes to the default remote branch (usually "origin" and "main")
git push

