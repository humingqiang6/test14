import mysql.connector
import os

def execute_select_query():
  """
  Connects to a MySQL database and executes a SELECT query.
  The connection details are read from environment variables.
  """
  try:
    # Read connection details from environment variables
    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    database = os.getenv("DB_NAME", "testdb")
    query = os.getenv("DB_QUERY", "SELECT 1;") # Default query

    # Establish connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = connection.cursor()
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Print results (or process them as needed)
    print("Query Results:")
    for row in results:
      print(row)

    # Close connections
    cursor.close()
    connection.close()

  except mysql.connector.Error as err:
    print(f"Error: {err}")
    if connection and connection.is_connected():
      cursor.close()
      connection.close()

if __name__ == "__main__":
  execute_select_query()