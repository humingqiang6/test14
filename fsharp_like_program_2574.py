import random

# Функция для обработки списка чисел: вычисление суммы квадратов четных чисел
def process_numbers(numbers):
    return sum(x**2 for x in numbers if x % 2 == 0)

# Пример списка чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = process_numbers(numbers)
print(f"Сумма квадратов четных чисел: {result}")

# Сохраняем список и результат в файл со случайным именем
with open('processed_numbers_result.txt', 'w') as f:
    f.write(f"Список: {numbers}\n")
    f.write(f"Результат обработки (сумма квадратов четных): {result}\n")

print("Результаты сохранены в 'processed_numbers_result.txt'")