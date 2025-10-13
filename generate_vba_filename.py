import random
import string

# Generate a random filename for the VBA module
random_filename = "Module" + ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ".bas"
print(random_filename)