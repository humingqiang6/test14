import random
import string

# Генерируем случайное имя файла длиной 10 символов
random_filename = "process_list_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + ".txt"
print(random_filename)