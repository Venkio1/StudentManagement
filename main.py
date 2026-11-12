import student

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        student.add_student()
    elif choice == "2":
        student.display_students()
    elif choice == "3":
        student.search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice\n")

