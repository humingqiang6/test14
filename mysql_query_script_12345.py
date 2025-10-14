import mysql.connector
from mysql.connector import Error
import os

def execute_select_query():
    """Connects to MySQL and executes a SELECT query."""
    connection = None
    cursor = None
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),  # Use environment variable or default
            database=os.getenv('DB_NAME', 'your_database'),
            user=os.getenv('DB_USER', 'your_username'),
            password=os.getenv('DB_PASSWORD', 'your_password')
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            cursor = connection.cursor()
            # Example SELECT query - modify as needed
            select_query = "SELECT * FROM your_table_name LIMIT 5;"
            cursor.execute(select_query)
            records = cursor.fetchall()

            print("Records from the table:")
            for row in records:
                print(row)

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the cursor and connection
        if cursor is not None and cursor.is_connected():
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    execute_select_query()