import sqlite3
import random
import string

# Generate a random table name
def random_table_name():
    return 'table_' + ''.join(random.choices(string.ascii_lowercase, k=10))

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table with a random name
table_name = random_table_name()
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        value REAL
    )
''')

print(f"Created table: {table_name}")

# Commit changes and close the connection
conn.commit()
conn.close()
