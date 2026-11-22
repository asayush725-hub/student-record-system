import json
from pathlib import Path


def load_students(filepath: str) -> list[dict]:
    """Load student records from a JSON file safely."""
    path = Path(filepath)
    students: list[dict] = []

    try:
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                students = data
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Warning: Could not load records ({exc}). Starting with an empty list.")
        students = []
    finally:
        pass

    return students


def save_students(filepath: str, students: list[dict]) -> bool:
    """Save student records to a JSON file using try-except-finally."""
    path = Path(filepath)
    saved = False

    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        saved = True
    except OSError as exc:
        print(f"Error: Failed to save records ({exc}).")
    finally:
        print(f"[Storage check] Save attempt finished for '{path.name}'.")

    return saved