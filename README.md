# Task Management System

A simple Python-based task management system with a command-line interface.

## Features

- **Add Tasks**: Create new tasks with title, description, and due date
- **Mark Complete**: Mark tasks as complete
- **View Pending**: Display all pending tasks
- **Track Progress**: Calculate and display completion percentage

## Project Structure

```
task_manager/
├── __init__.py
├── task_utility.py      # Core task functions
└── validation.py        # Input validation functions
main.py                  # Main entry point with menu
```

## Usage

```bash
python3 main.py
```

Follow the on-screen menu to:
1. Add a new task
2. Mark a task as complete
3. View pending tasks
4. Calculate progress
5. Exit

## Requirements

- Python 3.6+

## Date Format

Due dates must be in **YYYY-MM-DD** format (e.g., 2026-06-15).
