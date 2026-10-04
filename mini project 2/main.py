#Student Management System
import csv
import os

CSV_FILE = "students.csv"
FIELDNAMES = ["roll_no", "name", "marks"]


def initialize_file():
    """Ensure the CSV file exists with the proper header."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_students():
    """Read all students from the CSV file into a list of dicts."""
    initialize_file()
    students = []
    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students


def write_students(students):
    """Overwrite the CSV file with the updated list of students."""
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)


def add_student():
    roll_no = input("Enter Roll Number: ").strip()
    students = read_students()

    # Check if roll number already exists
    if any(s["roll_no"] == roll_no for s in students):
        print(f"Error: Roll number '{roll_no}' already exists.")
        return

    name = input("Enter Student Name: ").strip()
    marks = input("Enter Marks: ").strip()

    # Validate marks
    try:
        float(marks)
    except ValueError:
        print("Error: Marks must be a valid number.")
        return

    new_student = {"roll_no": roll_no, "name": name, "marks": marks}
    students.append(new_student)
    write_students(students)
    print(f"Student '{name}' added and saved successfully.")


def search_student():
    roll_no = input("Enter Roll Number to search: ").strip()
    students = read_students()

    for student in students:
        if student["roll_no"] == roll_no:
            print("\n--- Student Found ---")
            print(f"Roll Number : {student['roll_no']}")
            print(f"Name        : {student['name']}")
            print(f"Marks       : {student['marks']}")
            return

    print(f"No student found with Roll Number '{roll_no}'.")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ").strip()
    students = read_students()

    updated_students = [s for s in students if s["roll_no"] != roll_no]

    if len(updated_students) == len(students):
        print(f"Error: No student found with Roll Number '{roll_no}'.")
    else:
        write_students(updated_students)
        print(f"Student with Roll Number '{roll_no}' deleted and file updated.")


def view_all_students():
    students = read_students()
    if not students:
        print("No student records available.")
        return

    print("\n" + "=" * 45)
    print(f"{'Roll No':<12} {'Name':<22} {'Marks':<8}")
    print("=" * 45)
    for s in students:
        print(f"{s['roll_no']:<12} {s['name']:<22} {s['marks']:<8}")
    print("=" * 45)


def main():
    initialize_file()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Search Student by Roll No")
        print("3. Delete Student by Roll No")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            print("Exiting system. All data saved to students.csv.")
            break
        else:
            print("Invalid selection. Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()