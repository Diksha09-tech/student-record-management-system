
import json


# Load students from JSON file
def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


# Save students to JSON file
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


# Add student
def add_student():
    print("\n----- Add Student -----")

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")
    marks = input("Enter student marks: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    save_students()

    print("Student added successfully!")


# View students
def view_students():
    print("\n----- View Students -----")

    if len(students) == 0:
        print("No students found.")

    else:
        for student in students:
            print("\nID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])


# Search student
def search_student():
    print("\n----- Search Student -----")

    search = input("Enter student name: ")
    found = False

    for student in students:

        if search == student["name"]:
            print("\nStudent Found!")

            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])

            found = True
            break

    if found == False:
        print("Student not found.")


# Update student
def update_student():
    print("\n----- Update Student -----")

    search_id = input("Enter student ID: ")
    found = False

    for student in students:

        if search_id == student["id"]:

            print("Student found!")

            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["course"] = input("Enter new course: ")
            student["marks"] = input("Enter new marks: ")

            save_students()

            found = True

            print("Student updated successfully!")

            break

    if found == False:
        print("Student not found.")


# Delete student
def delete_student():
    print("\n----- Delete Student -----")

    search_id = input("Enter student ID: ")
    found = False

    for student in students:

        if search_id == student["id"]:

            students.remove(student)

            save_students()

            found = True

            print("Student deleted successfully!")

            break

    if found == False:
        print("Student not found.")


# Find top student
def top_student():
    print("\n----- Top Student -----")

    if len(students) == 0:
        print("No students found.")

    else:
        top = students[0]

        for student in students:

            if int(student["marks"]) > int(top["marks"]):
                top = student

        print("Top Student:", top["name"])
        print("Marks:", top["marks"])


# Calculate average marks
def average_marks():
    print("\n----- Average Marks -----")

    if len(students) == 0:
        print("No students found.")

    else:
        total = 0

        for student in students:
            total = total + int(student["marks"])

        average = total / len(students)

        print("Average Marks:", average)


# Load existing students
students = load_students()


# Main menu
while True:

    print("\n============================================")
    print("          STUDENT RECORD SYSTEM")
    print("============================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Find Top Student")
    print("7. Calculate Average Marks")
    print("8. Exit")

    choice = input("Enter number: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        top_student()

    elif choice == "7":
        average_marks()

    elif choice == "8":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

