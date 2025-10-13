#!/bin/bash

# Generate a random filename
randomFileName="processes_$(shuf -i 1-10000 -n 1).csv"

# Get the list of processes and save to the random filename
# Using ps aux and replacing spaces with commas for a simple CSV-like format
ps aux | tr ' ' ',' > "$randomFileName"

echo "Список процессов сохранен в файл: $randomFileName"