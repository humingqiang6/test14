import psycopg2
from psycopg2 import sql

def connect_to_db():
    """Connects to the PostgreSQL database server."""
    conn = None
    try:
        # --- Connection parameters ---
        # Replace these with your actual database credentials
        hostname = 'localhost'  # or your database server address
        database = 'your_database_name'
        username = 'your_username'
        password = 'your_password'
        port = '5432'  # default PostgreSQL port
        # -----------------------------

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=hostname,
            database=database,
            user=username,
            password=password,
            port=port
        )

        cur = conn.cursor()

        # Example: Print PostgreSQL version
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(f"PostgreSQL database version: {db_version[0]}")

        # Close the cursor
        cur.close()

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")

    finally:
        # Close the connection
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect_to_db()
