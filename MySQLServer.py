import mysql.connector
from mysql.connector import errorcode

# Database configuration
DB_NAME = 'alx_book_store'
config = {
    'user': 'your_username',    # replace with your MySQL username
    'password': 'your_password', # replace with your MySQL password
    'host': 'localhost',         # replace with your MySQL host if different
}

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Attempt to create the database
    try:
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"Database '{DB_NAME}' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database '{DB_NAME}' already exists.")
        else:
            print(f"Failed to create database '{DB_NAME}': {err}")

except mysql.connector.Error as err:
    print(f"Error connecting to the database: {err}")
finally:
    # Close the cursor and connection if they were created
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
