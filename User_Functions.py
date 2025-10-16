# Teacher Functions
def export_to_csv():
    import csv
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

