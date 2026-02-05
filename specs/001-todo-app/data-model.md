# Data Model: Todo App

**Feature**: Todo App (001-todo-app)
**Date**: 2025-12-30
**Input**: Feature specification from `specs/001-todo-app/spec.md`

## Entity Definitions

### TodoItem

Represents a single todo item with attributes as specified in the requirements.

**Attributes**:
- `id` (integer): Unique identifier assigned automatically when created
- `title` (string): Title of the todo item (required, non-empty)
- `description` (string): Description of the todo item (optional, can be empty)
- `completed` (boolean): Completion status (default: false)

**Validation Rules**:
- `id`: Must be a positive integer, unique within the session
- `title`: Must be a non-empty string after trimming whitespace
- `description`: Can be any string (including empty)
- `completed`: Must be a boolean value

**State Transitions**:
- `completed` can transition from `false` to `true` (complete operation)
- `completed` can transition from `true` to `false` (incomplete operation)
- `title` and `description` can be updated while preserving `id`
- `id` remains constant throughout the item's lifetime

### TodoService Data Structure

**In-Memory Storage**:
- `todos` (dict): Dictionary with `id` as key and `TodoItem` object as value
- `next_id` (integer): Counter for generating unique IDs, starts at 1

## Relationships

- `TodoService` contains multiple `TodoItem` instances
- Each `TodoItem` has a unique `id` within the `TodoService` context
- No cross-references between `TodoItem` instances

## Constraints

1. **Uniqueness**: Each `TodoItem.id` must be unique within the service instance
2. **Immutability**: `TodoItem.id` cannot be changed after creation
3. **Validation**: `TodoItem.title` must not be empty (after trimming)
4. **Persistence**: Data exists only in memory during runtime (no persistence)
5. **Thread Safety**: Not required as per single-user requirement

## Serialization

**To Dictionary**:
- `TodoItem` can be converted to a dictionary representation with all attributes
- Keys: "id", "title", "description", "completed"

**From Dictionary**:
- `TodoItem` can be reconstructed from a dictionary with the same keys
- Validation occurs during reconstruction to ensure data integrity