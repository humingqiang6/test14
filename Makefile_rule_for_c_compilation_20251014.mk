# Makefile для компиляции программы на C

# Имя исполняемого файла
TARGET = my_program

# Исходные файлы C
SOURCES = main.c utils.c

# Компилятор
CC = gcc

# Флаги компиляции
CFLAGS = -Wall -Wextra -std=c99

# Правило для сборки цели
$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCES)

# Правило для очистки
clean:
	rm -f $(TARGET)

# Псевдоним для сборки
build: $(TARGET)

# Псевдоним для запуска
run: $(TARGET)
	./$(TARGET)