import json

AKSHAY_FILE = "Akshay.json"


def load_students_details():
    try:
        with open(AKSHAY_FILE, 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    return students


def save_students(students):
    with open(AKSHAY_FILE, 'w') as file:
        json.dump(students, file, indent=4)


def add_student_details():
    candidate = input("Enter student's name: ")
    years = int(input("Enter student's age: "))
    percentage = input("Enter student's grade: ")
    email = input("Enter student's mail details: ")

    students = load_students_details()
    students.append({"name": candidate, "age": years, "grade": percentage, "mail": email})
    save_students(students)
    print("Student record added successfully!")


def view_students_details():
    students = load_students_details()
    if students:
        print("\nStudent records:")
        for student in students:
            print(f"Name: {student['name']} , Age:{student['age']}, Grade: {student['grade']}, Mail:  {student['mail']}")
    else:
        print("No student records found.")


def fetch_student_details():
    probe = input("Enter the name or grade of the student to fetch: ")

    students = load_students_details()
    found_students_details = []
    for student in students:
        if probe.lower() in student['name'].lower() or probe.lower() == student['grade'].lower():
            found_students_details.append(student)

    if found_students_details:
        print("\nFound Students:")
        for student in found_students_details:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Mail: {student['mail']}")
    else:
        print("No matching student records found.")


def update_student_details():
    probe = input("Enter the current name or grade of the student: ")

    students = load_students_details()
    for student in students:
        if probe.lower() == student['name'].lower() or student['grade'].lower():
            print(f"Student found: Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Mail: {student['mail']}")
            updated_age = int(input("Enter updated age: "))
            updated_grade = input("Enter updated grade: ")
            updated_mail = input("Enter updated mail details: ")
            student['age'] = updated_age
            student['grade'] = updated_grade
            student['mail'] = updated_mail
            save_students(students)
            print("Student record updated successfully!")
            return
    print("No matching student details found.")


def delete_student_details():
    probe = input("Enter the name of the student to delete: ")

    students = load_students_details()
    updated_students_details = [student for student in students if probe.lower() not in student['name'].lower()]

    if len(updated_students_details) < len(students):
        save_students(updated_students_details)
        print("Student record deleted successfully!")
    else:
        print("There is no record available for this student!")


def main_module():
    while True:
        print("\nStudent management system")
        print("1. Add student details")
        print("2. View students details")
        print("3. Search student details")
        print("4. Current student details")
        print("5. Remove student details")
        print("0. Close the tab")

        option = input("Enter your option: ")

        if option == '1':
            add_student_details()
        elif option == '2':
            view_students_details()
        elif option == '3':
            fetch_student_details()
        elif option == '4':
            update_student_details()
        elif option == '5':
            delete_student_details()
        elif option == '0':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_module()