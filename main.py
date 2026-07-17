from student_manager import StudentManager
manager = StudentManager()
while True:
    print("\n=================== STUDENT RECORD MANAGER ===================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.view_students()
    elif choice == "3":
        manager.search_student()
    elif choice == "4":
        manager.update_student()
    elif choice == "5":
        manager.delete_student()
    elif choice == '6':
        manager.generate_report()
    elif choice == "7":
        print("Thank you for using Student Record Manager!")
        break
    else:
        print("Invalid choice. Please try again.")