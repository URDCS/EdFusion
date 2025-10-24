import User_Functions
import time

while True:
    print("===== Student Management System =====")
    print("Login as:")
    print("1. Teacher")
    print("2. Student")
    print("3. Exit")

    user_type = input("Enter choice: ").strip()

    if user_type == "1":  # Teacher/Admin
        while True:
            print("\n--- Teacher Menu ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Calculate Grade")
            print("4. Export to CSV")
            print("5. Access Report")
            print("6. Generate Ranklist")
            print("7. Back to Login Menu")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                User_Functions.data_entry()
            elif choice == "2":
                User_Functions.extract_data()
            elif choice == "3":
                User_Functions.grade()
            elif choice == "4":
                User_Functions.export_to_csv()
            elif choice == "5":
                User_Functions.load_classreport()
            elif choice == "6":
                User_Functions.generate_ranklist()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Try again.")

    elif user_type == "2":  # Student/Viewer
        while True:
            print("\n--- Student Menu ---")
            print("1. Access student report")
            print("2. Back to Login Menu")
            choice = input("Enter choice : ").strip()
            if choice == "1":
                User_Functions.load_studentreport()
            elif choice == "2":
                break
            else:
                print("Invalid choice. Try again.")

    elif user_type == "3":  # Exit
        print("Exiting program...")
        time.sleep(3) #For extra dramatic effect as per hollywood standards
        break

    else:
        print("Invalid choice. Try again.")
