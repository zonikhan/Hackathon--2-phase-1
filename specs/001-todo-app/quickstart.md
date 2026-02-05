# Quickstart Guide: Todo App

**Feature**: Todo App (001-todo-app)
**Date**: 2025-12-30
**Input**: Feature specification from `specs/001-todo-app/spec.md`

## Getting Started

This guide provides quick instructions for setting up and using the Todo App command-line interface.

## Installation

1. Navigate to the project root directory
2. Install the application in development mode:
   ```bash
   pip install -e .
   ```

## Basic Usage

### Add a Todo Item
```bash
todo-app add --title "My task" --description "Task details here"
```
- `--title` is required
- `--description` is optional

### List All Todo Items
```bash
todo-app list
```
- Shows all todo items with ID, title, description, and completion status

### Update a Todo Item
```bash
todo-app update --id 1 --title "Updated title" --description "Updated description"
```
- `--id` is required (integer)
- `--title` and `--description` are optional (at least one required)

### Delete a Todo Item
```bash
todo-app delete --id 1
```
- `--id` is required (integer)

### Mark a Todo as Complete
```bash
todo-app complete --id 1
```
- `--id` is required (integer)

### Mark a Todo as Incomplete
```bash
todo-app incomplete --id 1
```
- `--id` is required (integer)

## Example Workflow

```bash
# Add a new todo
todo-app add --title "Buy groceries" --description "Milk, bread, eggs"

# Add another todo
todo-app add --title "Walk the dog"

# List all todos
todo-app list

# Mark first todo as complete
todo-app complete --id 1

# Update the second todo
todo-app update --id 2 --description "Take dog to the park"

# List all todos again to see changes
todo-app list
```

## Help and Information

To see all available commands and options:
```bash
todo-app --help
```

To see help for a specific command:
```bash
todo-app add --help
todo-app list --help
todo-app update --help
# etc.
```

## Important Notes

- Data is stored only in memory and is lost when the application exits
- Each session starts with a clean slate
- IDs are automatically assigned and are unique within each session
- All commands provide clear success or error messages