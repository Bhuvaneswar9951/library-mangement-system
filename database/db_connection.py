import mysql.connector

DB_CONFIG = {
    "host": "localhost", # Change if using a remote server 
    "user": "root", # Change if using a different MySQL user
    "password": "Bhuvan@143", # Update with MySQL password
    "database": "library_management"
}

def get_db_connection():
    """Establishes a database connection and returns the connection object"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("Database connection successful")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Test the connection
if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        connection.close()
