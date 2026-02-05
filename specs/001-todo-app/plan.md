# Implementation Plan: Todo App

**Branch**: `001-todo-app` | **Date**: 2025-12-30 | **Spec**: [specs/001-todo-app/spec.md](../specs/001-todo-app/spec.md)

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a command-line todo application with in-memory storage that provides core CRUD functionality (Add, List, Update, Delete, Mark Complete/Incomplete). The application follows clean architecture with separation of concerns between models, services, and CLI interface, implemented in Python 3.13+ with standard library only.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Standard Python library only (argparse, sys, typing)
**Storage**: In-memory only (dict-based, no persistence beyond runtime)
**Testing**: N/A (Phase I constraints - no testing frameworks)
**Target Platform**: Linux/WSL 2 Ubuntu 22.04 (console-based)
**Project Type**: Console application
**Performance Goals**: Immediate response for all operations (sub-second)
**Constraints**: <200ms response time, <100MB memory usage, no external dependencies
**Scale/Scope**: Single-user, single-session application

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

1. **Spec-Driven Development**: All implementation must originate from the specification at `specs/001-todo-app/spec.md`
2. **AI-Native Development**: All code generation must be performed using Claude Code
3. **Clean Architecture**: Must maintain separation of concerns (models, services, CLI)
4. **Deterministic Behavior**: Application must exhibit consistent behavior across executions
5. **Console-Based Interface**: Must be command-line driven only
6. **Technical Constraints**: Python 3.13+, standard library only, in-memory storage only
7. **Phase I Scope**: Must implement only Add, List, Update, Delete, Mark Complete/Incomplete features

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   └── todo_item.py     # TodoItem model definition
├── services/
│   └── todo_service.py  # Business logic and in-memory storage
└── cli/
    └── main.py          # Command-line interface using argparse
```

tests/
├── contract/
├── integration/
└── unit/

pyproject.toml           # Project configuration and CLI entry point
```

**Structure Decision**: Single project structure chosen to align with requirements. Clean architecture enforced with clear separation: models define data structures, services contain business logic and data management, CLI handles user interaction and command parsing.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| | | |

## Phase 0: Research & Architecture Decisions

### Key Technical Decisions to Document

1. **Todo Item Data Structure**: How to represent a todo item in memory
2. **ID Generation Strategy**: How to generate unique IDs for todo items
3. **Separation of CLI and Business Logic**: How to separate command-line interface from business logic
4. **Error Handling Approach**: How to handle invalid inputs and edge cases
5. **User Input Validation Strategy**: How to validate user input before processing

### Architecture Sketch

The application follows a clean architecture pattern with three main layers:

- **Models Layer**: Contains the `TodoItem` class that represents a single todo item with ID, title, description, and completion status
- **Services Layer**: Contains the `TodoService` class that handles all business logic, in-memory storage, and validation
- **CLI Layer**: Contains the command-line interface that parses user input and interacts with the service layer

Data flows from CLI → Service → Model, with error handling and validation at each layer.

### Component Responsibilities

- **TodoItem Model**: Represents a single todo item, validates data integrity, provides string representation
- **TodoService**: Manages in-memory storage (dictionary), implements CRUD operations, handles validation and error cases
- **CLI Main**: Parses command-line arguments, routes commands to service, formats output for user

## Phase 1: Design & Contracts

### Data Model (data-model.md)

Based on the specification, the key entity is:

**TodoItem**:
- id: integer (unique, auto-generated)
- title: string (required, non-empty)
- description: string (optional, can be empty)
- completed: boolean (default: false)

**TodoService**:
- todos: dictionary (key: id, value: TodoItem)
- next_id: integer (counter for unique ID generation)

### API Contracts (contracts/)

Since this is a CLI application, the "contracts" are the command-line interface specifications:

- `add` command: `--title <required> --description <optional>`
- `list` command: no parameters
- `update` command: `--id <required> --title <optional> --description <optional>`
- `delete` command: `--id <required>`
- `complete` command: `--id <required>`
- `incomplete` command: `--id <required>`

### Quickstart Guide (quickstart.md)

1. Install the application: `pip install -e .`
2. Add a todo: `todo-app add --title "My task" --description "Task details"`
3. List todos: `todo-app list`
4. Update a todo: `todo-app update --id 1 --title "Updated title"`
5. Mark complete: `todo-app complete --id 1`
6. Delete a todo: `todo-app delete --id 1`