# task_manager/validation.py

def validate_task_title(title):
    """Ensure the title is a non-empty string."""
    if isinstance(title, str) and len(title.strip()) > 0:
        return True
    raise ValueError("Error: Title cannot be empty.")

def validate_task_description(description):
    """Ensure the description is a non-empty string."""
    if isinstance(description, str) and len(description.strip()) > 0:
        return True
    raise ValueError("Error: Description cannot be empty.")

def validate_due_date(due_date):
    """
    Ensure the due date is in the YYYY-MM-DD format.
    """
    from datetime import datetime
    if not isinstance(due_date, str) or len(due_date.strip()) == 0:
        raise ValueError("Error: Due date cannot be empty.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Error: Due date must be in YYYY-MM-DD format.")