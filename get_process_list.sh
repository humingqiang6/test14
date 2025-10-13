#!/bin/bash

# Генерация случайного имени файла
random_filename="process_list_$(date +%s%N).txt"

# Получение списка процессов и сохранение в файл
ps aux > "$random_filename"

echo "Список процессов сохранен в файл: $random_filename"