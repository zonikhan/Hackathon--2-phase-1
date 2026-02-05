"""
Todo Service
Business logic for add, update, delete, mark operations
"""

from src.models.todo_item import TodoItem


class TodoService:
    def __init__(self):
        """
        Initialize the TodoService with an empty list of todos and ID counter
        """
        self.todos = []
        self.next_id = 1

    def add_todo(self, title, description=""):
        """
        Adds a new todo item to the collection

        Args:
            title (str): Title of the todo item (required)
            description (str): Description of the todo item (optional, defaults to empty string)

        Returns:
            int: The unique ID of the newly created todo item

        Raises:
            ValueError: If title is empty or only whitespace
        """
        # Create new todo item - this will validate the title
        todo_item = TodoItem(self.next_id, title, description, completed=False)

        # Add to collection
        self.todos.append(todo_item)

        # Increment ID counter
        todo_id = self.next_id
        self.next_id += 1

        return todo_id

    def list_todos(self):
        """
        Retrieves all todo items in the collection

        Returns:
            List[dict]: List of todo items with all fields (id, title, description, completed)
        """
        return [todo.to_dict() for todo in self.todos]

    def get_todo(self, todo_id):
        """
        Retrieves a specific todo item by its ID

        Args:
            todo_id (int): The unique ID of the todo item to retrieve

        Returns:
            dict: The todo item with all fields (id, title, description, completed)

        Raises:
            KeyError: If todo_id does not exist
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo.to_dict()

        raise KeyError(f"Todo with ID {todo_id} does not exist")

    def update_todo(self, todo_id, title=None, description=None):
        """
        Updates the title and/or description of an existing todo item

        Args:
            todo_id (int): The unique ID of the todo item to update
            title (str, optional): New title for the todo item (if None, title is unchanged)
            description (str, optional): New description for the todo item (if None, description is unchanged)

        Returns:
            bool: True if update was successful, False if todo_id does not exist

        Raises:
            ValueError: If title is empty or only whitespace (when updating title)
        """
        for todo in self.todos:
            if todo.id == todo_id:
                todo.update(title=title, description=description)
                return True

        return False

    def delete_todo(self, todo_id):
        """
        Removes a todo item from the collection

        Args:
            todo_id (int): The unique ID of the todo item to delete

        Returns:
            bool: True if deletion was successful, False if todo_id does not exist

        Side Effects:
            Reduces collection size by 1 if successful
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True

        return False

    def mark_complete(self, todo_id):
        """
        Marks a todo item as complete

        Args:
            todo_id (int): The unique ID of the todo item to mark as complete

        Returns:
            bool: True if operation was successful, False if todo_id does not exist

        Side Effects:
            Changes the 'completed' field of the todo item to True
        """
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = True
                return True

        return False

    def mark_incomplete(self, todo_id):
        """
        Marks a todo item as incomplete

        Args:
            todo_id (int): The unique ID of the todo item to mark as incomplete

        Returns:
            bool: True if operation was successful, False if todo_id does not exist

        Side Effects:
            Changes the 'completed' field of the todo item to False
        """
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = False
                return True

        return False