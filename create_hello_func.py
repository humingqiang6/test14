import random
import string

def generate_random_filename(ext='.py'):
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f'{name}{ext}'

def hello_world_func():
    print('Привет, мир!')

random_filename = generate_random_filename()
with open(random_filename, 'w', encoding='utf-8') as f:
    f.write('def hello_world_func():\n    print("Привет, мир!")\n\n# Вызов функции\nhello_world_func()\n')

print(random_filename)