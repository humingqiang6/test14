import os
import random
import string
import shutil

# Define source file
source_file = '/workspace/numbers.f90'

# Generate a random filename (e.g., random_letters_12345.f90)
random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.f90'
destination_file = os.path.join('/workspace', random_name)

# Move (rename) the file to the new random name
shutil.move(source_file, destination_file)

print(f"Файл программы Fortran сохранен под случайным именем: {destination_file}")