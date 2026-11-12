students = []

def validate_student(name, age, department):
    if name == "":
        print("Invalid student name")
        return False
    if age < 17 or age > 30:
        print("Invalid age")
        return False
    if department == "":
        print("Invalid department")
        return False
    print("Student details are valid")
    return True

def add_student():
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    
    if validate_student(name, age, department):
        students.append({"id": sid, "name": name, "age": age, "department": department})
        print("Student added!\n")

def display_students():
    for s in students:
        print(s["id"], "-", s["name"], "-", s["age"], "-", s["department"])
    print()

def search_student():
    sid = input("Enter ID to search: ")
    for s in students:
        if s["id"] == sid:
            print("Found:", s["name"], "-", s["age"], "-", s["department"], "\n")
            return
    print("Student not found.\n")

# Temporary test cases
if __name__ == "__main__":
    validate_student("Arun", 20, "CSE")
    validate_student("", 20, "CSE")
    validate_student("Arun", 15, "CSE")

