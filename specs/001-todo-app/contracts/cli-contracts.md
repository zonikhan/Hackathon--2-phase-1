# CLI Contracts: Todo App

**Feature**: Todo App (001-todo-app)
**Date**: 2025-12-30
**Input**: Feature specification from `specs/001-todo-app/spec.md`

## Command Interface Specifications

### Add Command
- **Command**: `todo-app add`
- **Parameters**:
  - `--title` (required, string): Title of the todo item
  - `--description` (optional, string): Description of the todo item
- **Success Response**: Todo item created with unique ID and default incomplete status
- **Error Responses**:
  - Title is empty: Error message to stderr
  - Invalid input format: Error message to stderr
- **Output Format**: Success message with created todo details

### List Command
- **Command**: `todo-app list`
- **Parameters**: None
- **Success Response**: List of all todo items with ID, title, description, and completion status
- **Error Responses**: None (empty list is valid)
- **Output Format**: Formatted list with status indicators

### Update Command
- **Command**: `todo-app update`
- **Parameters**:
  - `--id` (required, integer): ID of the todo item to update
  - `--title` (optional, string): New title for the todo item
  - `--description` (optional, string): New description for the todo item
- **Success Response**: Updated todo item details
- **Error Responses**:
  - Todo with ID doesn't exist: Error message to stderr
  - Title is empty (if provided): Error message to stderr
- **Output Format**: Success message with updated todo details

### Delete Command
- **Command**: `todo-app delete`
- **Parameters**:
  - `--id` (required, integer): ID of the todo item to delete
- **Success Response**: Confirmation that todo was deleted
- **Error Responses**:
  - Todo with ID doesn't exist: Error message to stderr
- **Output Format**: Success or error message

### Complete Command
- **Command**: `todo-app complete`
- **Parameters**:
  - `--id` (required, integer): ID of the todo item to mark complete
- **Success Response**: Todo item marked as complete
- **Error Responses**:
  - Todo with ID doesn't exist: Error message to stderr
- **Output Format**: Success message with updated todo details

### Incomplete Command
- **Command**: `todo-app incomplete`
- **Parameters**:
  - `--id` (required, integer): ID of the todo item to mark incomplete
- **Success Response**: Todo item marked as incomplete
- **Error Responses**:
  - Todo with ID doesn't exist: Error message to stderr
- **Output Format**: Success message with updated todo details

## Common Error Handling

### Input Validation
- Invalid command: Show help and exit with error code
- Missing required parameters: Show error and exit with error code
- Invalid parameter types: Show error and exit with error code

### Output Standards
- Success messages to stdout
- Error messages to stderr
- Use clear, user-friendly language
- Include relevant IDs or identifiers in output when possible

## Exit Codes
- 0: Success
- 1: General error
- 2: Command-line usage error