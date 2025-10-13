import os
import uuid

# Generate a random filename
random_filename = f"{str(uuid.uuid4())}.py"

# Source script to copy
source_script = "/workspace/api_script_template.py"

# Destination path with the random name
destination_script = f"/workspace/{random_filename}"

# Copy the content from the source to the destination
with open(source_script, 'rb') as src_file:
    content = src_file.read()

with open(destination_script, 'wb') as dest_file:
    dest_file.write(content)

print(f"Original script: {source_script}")
print(f"New random script name: {destination_script}")
