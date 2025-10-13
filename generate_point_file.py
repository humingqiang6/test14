import struct
import random
import string

# Генерация случайного имени файла
random_filename = "point_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".bin"

# Определение структуры точки
point_data = {
    'x': 5.0,
    'y': 10.0
}

# Запись данных в бинарный файл
with open(random_filename, 'wb') as f:
    # Упаковка чисел с плавающей запятой двойной точности (64-бит)
    f.write(struct.pack('d', point_data['x']))
    f.write(struct.pack('d', point_data['y']))

print(f"Файл с данными точки создан: {random_filename}")