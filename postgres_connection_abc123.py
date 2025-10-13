import psycopg2

# Connection parameters
conn_params = {
    "host": "localhost",
    "database": "your_database_name",
    "user": "your_username",
    "password": "your_password",
    "port": "5432"  # Default PostgreSQL port
}

try:
    # Establish the connection
    connection = psycopg2.connect(**conn_params)

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a simple query
    cursor.execute('SELECT version();')

    # Fetch the result
    db_version = cursor.fetchone()
    print(f"PostgreSQL version: {db_version[0]}")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print(f"An error occurred: {e}")