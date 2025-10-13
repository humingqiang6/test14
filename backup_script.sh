#!/bin/bash

# Проверяем, передан ли аргумент
if [ $# -eq 0 ]; then
    echo "Ошибка: не указан файл для резервного копирования."
    echo "Использование: $0 <путь_к_файлу>"
    exit 1
fi

SOURCE_FILE="$1"

# Проверяем, существует ли файл
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Ошибка: файл $SOURCE_FILE не существует."
    exit 1
fi

# Генерируем случайное имя для файла резервной копии
BACKUP_NAME=$(mktemp --suffix=.bak)

# Копируем файл
cp "$SOURCE_FILE" "$BACKUP_NAME"

if [ $? -eq 0 ]; then
    echo "Файл $SOURCE_FILE успешно скопирован в $BACKUP_NAME"
else
    echo "Ошибка при копировании файла."
    exit 1
fi