#!/bin/bash

# Script to create a backup of a file with a random name

if [ $# -ne 1 ]; then
  echo "Usage: $0 <file_to_backup>"
  exit 1
fi

FILE_TO_BACKUP="$1"

if [ ! -f "$FILE_TO_BACKUP" ]; then
  echo "Error: File '$FILE_TO_BACKUP' does not exist."
  exit 1
fi

# Generate a random filename for the backup
BACKUP_NAME="/workspace/backup_$(openssl rand -hex 8).bak"

# Create the backup
cp "$FILE_TO_BACKUP" "$BACKUP_NAME"

if [ $? -eq 0 ]; then
  echo "Backup created successfully: $BACKUP_NAME"
else
  echo "Error creating backup."
  exit 1
fi