import mysql.connector
from mysql.connector import Error
import uuid

def execute_select_query():
    """
    Connects to a MySQL database and executes a SELECT query.
    Results are printed to the console.
    The script name is randomly generated at runtime.
    """
    # Generate a random script name for demonstration
    random_script_name = f"query_script_{uuid.uuid4().hex[:8]}.py"
    print(f"This script is conceptually named: {random_script_name}")

    connection = None
    try:
        # Configuration: Replace these with your actual database details
        config = {
            'host': 'localhost',  # Or your MySQL server address
            'database': 'your_database_name',
            'user': 'your_username',
            'password': 'your_password',
            'port': 3306  # Default MySQL port
        }

        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            cursor = connection.cursor()
            # Example SELECT query - modify as needed
            select_query = "SELECT * FROM your_table_name LIMIT 5;"
            cursor.execute(select_query)

            records = cursor.fetchall()
            print(f"\nQuery executed: {select_query}")
            print("Results:")
            for row in records:
                print(row)

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("\nMySQL connection is closed.")

if __name__ == "__main__":
    execute_select_query()
