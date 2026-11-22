from records import (
    add_student,
    delete_student,
    search_students,
    sort_students,
    update_student,
)
from storage import load_students, save_students

DATA_FILE = "students.json"


def display_students(students: list[dict]) -> None:
    """Print student records in a clean table format."""
    if not students:
        print("\nNo student records found.")
        return

    print("\nID    | Name                 | Course          | Marks")
    print("-" * 58)
    for s in students:
        print(f"{s['id']:<5} | {s['name']:<20} | {s['course']:<15} | {s['marks']}")


def prompt_int(message: str) -> int:
    """Safely read an integer from user input."""
    while True:
        try:
            return int(input(message).strip())
        except ValueError:
            print("Invalid number. Please enter a whole number.")


def prompt_marks(message: str) -> float:
    """Safely read marks (0 to 100) from user input."""
    while True:
        try:
            value = float(input(message).strip())
            if 0 <= value <= 100:
                return value
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid marks. Please enter a numeric value.")


def run_app() -> None:
    """Run the interactive CLI menu loop."""
    students = load_students(DATA_FILE)

    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Students")
        print("4. Sort Students")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        try:
            if choice == "1":
                sid = prompt_int("Enter Student ID: ")
                name = input("Enter Name: ")
                course = input("Enter Course: ")
                marks = prompt_marks("Enter Marks (0-100): ")
                students, msg = add_student(students, sid, name, course, marks)
                print(msg)
                save_students(DATA_FILE, students)

            elif choice == "2":
                display_students(students)

            elif choice == "3":
                keyword = input("Enter name or course to search: ")
                results = search_students(students, keyword)
                display_students(results)

            elif choice == "4":
                field = input("Sort by (id / name / course / marks) [default: marks]: ").strip().lower() or "marks"
                order = input("Order (asc / desc) [default: desc]: ").strip().lower() or "desc"
                sorted_list = sort_students(students, sort_by=field, descending=(order != "asc"))
                display_students(sorted_list)

            elif choice == "5":
                sid = prompt_int("Enter Student ID to update: ")
                name = input("New Name (press Enter to keep current): ").strip() or None
                course = input("New Course (press Enter to keep current): ").strip() or None
                marks_input = input("New Marks (press Enter to keep current): ").strip()
                try:
                    marks = float(marks_input) if marks_input else None
                except ValueError:
                    raise ValueError("Marks must be a numeric value.")
                students, msg = update_student(students, sid, name=name, course=course, marks=marks)
                print(msg)
                save_students(DATA_FILE, students)

            elif choice == "6":
                sid = prompt_int("Enter Student ID to delete: ")
                students, msg = delete_student(students, sid)
                print(msg)
                save_students(DATA_FILE, students)

            elif choice == "7":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Please select a valid option between 1 and 7.")

        except ValueError as exc:
            print(f"Input error: {exc}")
        except Exception as exc:
            print(f"Unexpected error: {exc}")


if __name__ == "__main__":
    run_app()