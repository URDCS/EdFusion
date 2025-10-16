# Teacher Functions
from Databaseconnector import connect_to_database 
import mysql.connector
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

def export_to_csv():
    import csv
    cursor=connect_to_database.mydb.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    #Export full class report
    with open("students_report.csv", "a", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(["Roll No", "Name", "Grade", "Total_Marks"])  # column headers
        writer.writerows(rows)
    print("Class csv exported as students_report.csv\n")

def grade():
    P = float(input("Enter marks in Physics"))
    C = float(input("Enter marks in Chemistry"))
    M = float(input("Enter marks in Mathematics"))    
    E = float(input("Enter marks in English"))
    CS = float(input("Enter marks in Computer Science"))  
    total=P+C+M+E+CS
    if total>=450:
        print("Grade: A")
    elif total>=400:
        print("Grade: B")
    elif total>=350:
        print("Grade: C")
    elif total>=300:
        print("Grade: D")
    else:
        print("Grade: F")


def load_classreport():
    import os
    filename= "students_report.csv"
    if os.path.exists(filename):
        os.startfile(filename)
    else:
         print("CSV file not found. Export it first.")
                
def generate_ranklist():
    cursor=connect_to_database.mydb.cursor()
    cursor.execute("SELECT roll_no, name, maths, physics, chemistry, english, computerscience FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("No student records found!")
        return
    ranklist = []
    for row in rows:
        roll_no, name, maths, physics, chemistry, english, computerscience = row
        total = maths + physics + chemistry + english + computerscience
        percentage = total/5
        ranklist.append((roll_no, name, percentage, total))
    ranklist.sort(key=lambda x: x[-1], reverse=True) #This is because we want to sort acc to total, and not the first element, "therefore" we have to specify the key
    print("\n===== Ranklist =====")
    rank = 1
    for student in ranklist:
        roll_no, name, percentage, total = student
        print(rank, "\t", roll_no, "\t", name, "\t", percentage, "\t", total)
        rank += 1



#Student Functions
def get_student_rank(cursor, roll_no):
    ranklist = generate_ranklist()
    for rank, roll, name, percentage, total in ranklist:
        if roll == roll_no:
            return rank
    return "N/A"

def load_studentreport():
    rno=int(input("Enter your roll number: "))
    import csv
    import matplotlib.pyplot as plt
    cursor=connect_to_database.mydb.cursor()
    cursor.execute("SELECT roll_no, name, maths, physics, chemistry, english, computerscience FROM students WHERE roll_no=rno")
    row = cursor.fetchone()
    if row:
        roll, name, phy, chem, math, cs, eng = row
        total = phy + chem + math + cs + eng
        percentage = total / 5
        rank = get_student_rank(cursor, roll)
        filename = (name+"_report.csv")
        with open(filename, "w", newline="") as fp:
            writer = csv.writer(fp)
            writer.writerow(["Roll No", "Name", "Physics", "Chemistry", "Maths", "ComputerScience", "English", "Total", "Percentage", "Grade", "Rank"])
            writer.writerow([roll, name, phy, chem, math, cs, eng, total, percentage, grade, rank])

        #chart
        subjects = [ "Physics", "Chemistry", "Maths", "CS", "English"]
        marks = [phy, chem, math, cs, eng]
        plt.bar(subjects, marks, color="skyblue")
        plt.title("Performance Report - "+name)
        plt.xlabel("Subjects")
        plt.ylabel("Marks")
        plt.savefig(name+"_chart.png")
        plt.close()
        print("Report generated: ", filename, name+"_chart.png")
    else:
        print("No student found with that roll number.")

