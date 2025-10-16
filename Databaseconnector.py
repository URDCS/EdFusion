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

def extract_data(connection):
    """Extracts and prints data from a selected table."""
    if connection:
        cursor = None 
        try:
            cursor = connection.cursor()
            print("choose number to display table : 1 - 11A, 2 - 11B, 3 - 12A, 4 - 12B")
            while True:
                try:
                    choice = int(input("enter your choice: "))
                    if 1 <= choice <= 4:
                        break
                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            table_map = {
                1: "11A",
                2: "11B",
                3: "12A",
                4: "12B"
            }
            
            table_name = table_map[choice]
            
            # Execute the query for the chosen table
            cursor.execute(f"SELECT * FROM {table_name}")
            results = cursor.fetchall()
            
            print(f"\n--- Data from table: {table_name} ---")
            
            if results:
                for row in results:
                    print(row)
            else:
                print(f"No data found in {table_name}.")

        except mysql.connector.Error as err:
             print(f"Database Error: {err}")
        except Exception as err:
            print(f"General Error extracting data: {err}")
        finally:
            if cursor:
                cursor.close()
    else:
        print("Cannot extract data. Database connection is not established.")
if __name__ == "__main__":
    db_connection = connect_to_database()
    if db_connection:
        extract_data(db_connection)
        db_connection.close() # Close the connection when done
        print("\nDatabase connection closed.")
