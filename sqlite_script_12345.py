import sqlite3
import random
import string

# Generate a random table name
def random_table_name():
    return 'table_' + ''.join(random.choices(string.ascii_lowercase, k=8))

# Connect to SQLite database (or create it)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the table with a random name
table_name = random_table_name()
create_table_sql = f'''
CREATE TABLE IF NOT EXISTS "{table_name}" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
);
'''
cursor.execute(create_table_sql)

# Commit changes and close the connection
conn.commit()
conn.close()

print(f"Created table: {table_name}")