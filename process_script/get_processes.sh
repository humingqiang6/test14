#!/bin/bash
# Bash script to get processes and save to a file with a unique name based on timestamp
output_file="process_list_$(date +%s).csv"
# Use ps to get a list of processes and format it as CSV
echo "PID,PPID,USER,%CPU,%MEM,COMMAND" > "$output_file"
ps -eo pid,ppid,user,pcpu,pmem,comm --no-headers | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | awk '{print $1","$2","$3","$4","$5","$6}' >> "$output_file"
echo "Process list saved to $output_file"