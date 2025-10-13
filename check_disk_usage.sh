#!/bin/bash

# Check disk usage and alert if over 80%

# Get the disk usage percentage for the root filesystem
usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

# Check if usage is greater than 80
if [ "$usage" -gt 80 ]; then
    echo "ALERT: Disk usage is ${usage}%!"
    # You could add more actions here, like sending an email or logging to a file
else
    echo "Disk usage is ${usage}%, which is OK."
fi