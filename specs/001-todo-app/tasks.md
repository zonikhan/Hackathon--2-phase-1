---
description: "Task list template for feature implementation"
---

# Tasks: Todo App

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 [P] Create src directory structure: src/models/, src/services/, src/cli/
- [X] T003 [P] Initialize Python project with pyproject.toml for UV dependency management

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create TodoItem model in src/models/todo_item.py with id, title, description, completed fields
- [X] T005 Create TodoService in src/services/todo_service.py with in-memory storage
- [X] T006 Create basic CLI framework in src/cli/main.py to handle command-line arguments

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items with title, description, and default incomplete status

**Independent Test**: Can be fully tested by adding a new todo item and verifying it appears in the list with a unique ID and default incomplete status

### Implementation for User Story 1

- [X] T007 [P] [US1] Implement add_todo method in src/services/todo_service.py
- [X] T008 [US1] Implement 'add' command in src/cli/main.py to call add_todo service
- [X] T009 [US1] Add command-line argument parsing for 'add' command with title and description options
- [X] T010 [US1] Test adding todo with title and description works correctly
- [X] T011 [US1] Test adding todo with only title works correctly (empty description)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View/List Todo Items (Priority: P2)

**Goal**: Enable users to see all their todo items with their IDs, titles, and completion status indicators

**Independent Test**: Can be fully tested by adding one or more todo items and then viewing the list to confirm they appear correctly with their status indicators

### Implementation for User Story 2

- [X] T012 [P] [US2] Implement list_todos method in src/services/todo_service.py
- [X] T013 [US2] Implement 'list' command in src/cli/main.py to call list_todos service
- [X] T014 [US2] Format output to show ID, title, and completion status indicator for each todo
- [X] T015 [US2] Test listing todos when multiple items exist
- [X] T016 [US2] Test listing todos when no items exist (show appropriate message)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update and Manage Todo Items (Priority: P3)

**Goal**: Enable users to modify existing todo items (update title/description) and manage their status (mark complete/incomplete) or delete items

**Independent Test**: Can be fully tested by performing update, delete, and status change operations on existing items and verifying the changes are reflected in the system

### Implementation for User Story 3

- [X] T017 [P] [US3] Implement update_todo method in src/services/todo_service.py
- [X] T018 [P] [US3] Implement delete_todo method in src/services/todo_service.py
- [X] T019 [P] [US3] Implement mark_complete method in src/services/todo_service.py
- [X] T020 [P] [US3] Implement mark_incomplete method in src/services/todo_service.py
- [X] T021 [US3] Implement 'update' command in src/cli/main.py to call update_todo service
- [X] T022 [US3] Implement 'delete' command in src/cli/main.py to call delete_todo service
- [X] T023 [US3] Implement 'complete' command in src/cli/main.py to call mark_complete service
- [X] T024 [US3] Implement 'incomplete' command in src/cli/main.py to call mark_incomplete service
- [X] T025 [US3] Test updating existing todo item works correctly
- [X] T026 [US3] Test deleting existing todo item works correctly
- [X] T027 [US3] Test marking todo as complete works correctly
- [X] T028 [US3] Test marking todo as incomplete works correctly

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Error Handling and Edge Cases

**Goal**: Handle invalid inputs and edge cases gracefully

- [X] T029 [P] Add validation to prevent empty titles in add_todo and update_todo methods
- [X] T030 [P] Add error handling for operations on non-existent todo IDs
- [X] T031 Add proper error messages for all error cases
- [X] T032 Handle special characters in titles and descriptions properly
- [X] T033 Test error cases: updating/deleting non-existent items, empty titles

**Checkpoint**: Error handling is now implemented across all operations

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T034 [P] Improve CLI output formatting and readability
- [X] T035 Add help text and usage instructions to CLI commands
- [X] T036 Code cleanup and refactoring
- [X] T037 [P] Add basic documentation to functions and classes
- [X] T038 Run quickstart validation to ensure all commands work as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Error Handling (Phase 6)**: Depends on basic functionality from user stories
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence