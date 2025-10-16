import mysql.connector

def connect_to_database():
    """Connects to a MySQL database."""
    try:
        mydb = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL host
            user="your_username",  # Replace with your MySQL username
            password="your_password",  # Replace with your MySQL password
            database="your_database_name"  # Replace with your database name
        )
        print("Successfully connected to the database!")
        return mydb
    except mysql.connector.Error as err:
        print(f"Error connecting: {err}")
        return None

def extract_data(connection):
    """Extracts and prints data from a table."""
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM students")  # Replace 'students' with your table name
            results = cursor.fetchall()
            if results:
                print("Data from the table:")
                for row in results:
                    print(row)  # Print each row of data
            else:
                print("No data found in the table.")
        except mysql.connector.Error as err:
            print(f"Error extracting data: {err}")
        finally:
            cursor.close()

def main():
    """Main function to connect and extract data."""
    db_connection = connect_to_database()
    if db_connection:
        extract_data(db_connection)
        db_connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
