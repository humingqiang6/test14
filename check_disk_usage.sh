#!/bin/bash

# Check disk usage and alert if over 80%
THRESHOLD=80
USAGE=$(df / | grep / | awk '{ print $5}' | sed 's/%//g')

if [ $USAGE -gt $THRESHOLD ]; then
    echo "ALERT: Disk usage is at ${USAGE}%!"
    # You could add an email command here like `mail` or `sendmail`
    # Example: echo "Disk usage is high: ${USAGE}%" | mail -s "Disk Alert" user@example.com
else
    echo "Disk usage is normal: ${USAGE}%."
fi