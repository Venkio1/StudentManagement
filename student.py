students = []

def add_student():
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    students.append({"id": sid, "name": name, "course": course})
    print("Student added!\n")

def display_students():
    for s in students:
        print(s["id"], "-", s["name"], "-", s["course"])
    print()

def search_student():
    sid = input("Enter ID to search: ")
    for s in students:
        if s["id"] == sid:
            print("Found:", s["name"], "-", s["course"], "\n")
            return
    print("Student not found.\n")

