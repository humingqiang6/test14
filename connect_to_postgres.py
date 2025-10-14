import psycopg2
from psycopg2 import sql

def connect_to_db():
    """
    Connects to a PostgreSQL database using psycopg2.
    Replace the connection parameters with your actual database details.
    """
    try:
        # Connection parameters - replace these with your actual DB details
        connection = psycopg2.connect(
            host="localhost",      # e.g., 'localhost' or an IP address
            database="your_db_name",
            user="your_username",
            password="your_password",
            port="5432"            # default PostgreSQL port
        )

        cursor = connection.cursor()

        # Example query to test the connection
        cursor.execute('SELECT version();')
        db_version = cursor.fetchone()
        print(f"Connected to PostgreSQL database. Version: {db_version[0]}")

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return True

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        return False

if __name__ == "__main__":
    connect_to_db()