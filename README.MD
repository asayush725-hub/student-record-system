# Student Record Management System

A command-line **Student Record Management System** built in Python to perform full **CRUD (Create, Read, Update, Delete)** operations with persistent JSON storage.

## Features
- **Add Student:** Create new student records with unique ID validation.
- **View & Search:** Display all records in a formatted table or search by name/course using list comprehensions.
- **Sort Records:** Sort students dynamically by ID, name, course, or marks using `lambda` functions.
- **Update & Delete:** Modify existing student details or remove records safely.
- **Persistent Storage:** Automatically loads and saves student records to `students.json`.
- **Error Handling:** Gracefully handles invalid inputs and file I/O errors using `try-except-finally` blocks.

## Project Structure
```text
student_record_system/
├── main.py          # Interactive CLI menu and input validation
├── records.py       # CRUD operations, lambda sorting, and list comprehensions
├── storage.py       # JSON file read/write operations with exception handling
├── students.json    # Auto-generated JSON storage file
└── README.md        # Project documentation