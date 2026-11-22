def find_student_by_id(students: list[dict], student_id: int) -> dict | None:
    """Find a single student by ID using a list comprehension."""
    matches = [s for s in students if s.get("id") == student_id]
    return matches[0] if matches else None


def _validate_student(student_id: int, name: str, course: str, marks: float) -> None:
    """Validate common student-record fields."""
    if not isinstance(student_id, int) or isinstance(student_id, bool) or student_id < 0:
        raise ValueError("Student ID must be a non-negative whole number.")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name cannot be empty.")
    if not isinstance(course, str) or not course.strip():
        raise ValueError("Course cannot be empty.")
    if isinstance(marks, bool) or not isinstance(marks, (int, float)):
        raise ValueError("Marks must be a numeric value.")
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")


def add_student(students: list[dict], student_id: int, name: str, course: str, marks: float) -> tuple[list[dict], str]:
    """Create a new student record if the ID is unique."""
    _validate_student(student_id, name, course, marks)

    if find_student_by_id(students, student_id) is not None:
        return students, f"A student with ID {student_id} already exists."

    new_student = {
        "id": student_id,
        "name": name.strip(),
        "course": course.strip(),
        "marks": marks,
    }
    updated = [*students, new_student]
    return updated, f"Added student '{new_student['name']}' (ID: {student_id})."


def search_students(students: list[dict], keyword: str) -> list[dict]:
    """Search students by name or course using a list comprehension."""
    term = keyword.strip().lower()
    return [
        s for s in students
        if term in str(s.get("name", "")).lower() or term in str(s.get("course", "")).lower()
    ]


def sort_students(students: list[dict], sort_by: str = "marks", descending: bool = True) -> list[dict]:
    """Sort student records using a lambda key function."""
    valid_keys = {"id", "name", "course", "marks"}
    key_name = sort_by if sort_by in valid_keys else "marks"

    def sort_key(student: dict):
        value = student.get(key_name)
        if key_name in {"name", "course"}:
            return str(value).lower() if value is not None else ""
        if key_name == "marks":
            return value if isinstance(value, (int, float)) and not isinstance(value, bool) else float("-inf")
        return value if isinstance(value, int) and not isinstance(value, bool) else float("-inf")

    return sorted(
        students,
        key=sort_key,
        reverse=descending,
    )


def update_student(
    students: list[dict],
    student_id: int,
    name: str | None = None,
    course: str | None = None,
    marks: float | None = None,
) -> tuple[list[dict], str]:
    """Update fields of an existing student record."""
    if find_student_by_id(students, student_id) is None:
        return students, f"No student found with ID {student_id}."

    if name is not None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty.")
    if course is not None:
        if not isinstance(course, str) or not course.strip():
            raise ValueError("Course cannot be empty.")
    if marks is not None:
        if isinstance(marks, bool) or not isinstance(marks, (int, float)):
            raise ValueError("Marks must be a numeric value.")
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")

    updated_students = []
    for student in students:
        if student.get("id") == student_id:
            updated_students.append({
                "id": student["id"],
                "name": name.strip() if name else student["name"],
                "course": course.strip() if course else student["course"],
                "marks": marks if marks is not None else student["marks"],
            })
        else:
            updated_students.append(student)

    return updated_students, f"Updated student ID {student_id}."


def delete_student(students: list[dict], student_id: int) -> tuple[list[dict], str]:
    """Delete a student record by ID using a list comprehension."""
    if find_student_by_id(students, student_id) is None:
        return students, f"No student found with ID {student_id}."

    remaining = [s for s in students if s.get("id") != student_id]
    return remaining, f"Deleted student ID {student_id}."