"""
Todo Item Model
Represents a single task with unique ID, title, description, and completion status
"""

class TodoItem:
    # Maximum lengths for validation
    MAX_TITLE_LENGTH = 200
    MAX_DESCRIPTION_LENGTH = 1000

    def __init__(self, id, title, description="", completed=False):
        """
        Initialize a TodoItem instance

        Args:
            id (int): Unique identifier for the todo item
            title (str): Title of the todo item (required)
            description (str): Description of the todo item (optional, defaults to empty string)
            completed (bool): Completion status of the todo item (defaults to False)
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or only whitespace")

        if len(title) > self.MAX_TITLE_LENGTH:
            raise ValueError(f"Title exceeds maximum length of {self.MAX_TITLE_LENGTH} characters")

        if len(description) > self.MAX_DESCRIPTION_LENGTH:
            raise ValueError(f"Description exceeds maximum length of {self.MAX_DESCRIPTION_LENGTH} characters")

        self.id = id
        self.title = title.strip()
        self.description = description
        self.completed = completed

    def __str__(self):
        """String representation of the todo item"""
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title} - {self.description}"

    def to_dict(self):
        """Convert the todo item to a dictionary representation"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    def update(self, title=None, description=None):
        """
        Update the todo item's title and/or description

        Args:
            title (str, optional): New title for the todo item
            description (str, optional): New description for the todo item

        Raises:
            ValueError: If title is empty or only whitespace when updating
        """
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty or only whitespace")

            if len(title) > self.MAX_TITLE_LENGTH:
                raise ValueError(f"Title exceeds maximum length of {self.MAX_TITLE_LENGTH} characters")

            self.title = title.strip()

        if description is not None:
            if len(description) > self.MAX_DESCRIPTION_LENGTH:
                raise ValueError(f"Description exceeds maximum length of {self.MAX_DESCRIPTION_LENGTH} characters")

            self.description = description