# task_manager/validation.py

def validate_task_title(title):
    """Ensure the title is a non-empty string."""
    if isinstance(title, str) and title.strip():
        return True
    print("Error: Title cannot be empty.")
    return False

def validate_task_description(description):
    """Ensure the description is a non-empty string."""
    if isinstance(description, str) and description.strip():
        return True
    print("Error: Description cannot be empty.")
    return False

def validate_due_date(due_date):
    """
    Ensure the due date is in the YYYY-MM-DD format.
    """
    from datetime import datetime
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Due date must be in YYYY-MM-DD format.")
        return False