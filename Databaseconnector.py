import mysql.connector

def connect_to_database():
    """Establishes a connection to the MySQL database."""
    try:
        mydb = mysql.connector.connect(
            host="localhost", 
            user="root",  
            password="your_password", 
            database="school"
        )
        print("Successfully connected to the database!")
        return mydb
    except mysql.connector.Error as err:
        print(f"Error connecting: {err}")
        return None
