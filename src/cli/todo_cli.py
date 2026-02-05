"""
Todo CLI
Command-line interface for user interaction
"""

from src.services.todo_service import TodoService


class TodoCLI:
    def __init__(self):
        """
        Initialize the TodoCLI with a TodoService instance
        """
        self.service = TodoService()

    def display_menu(self):
        """
        Display the main menu options to the user
        """
        print("\n=== Todo Application ===")
        print("1. Add a new todo item")
        print("2. View all todo items")
        print("3. Update a todo item")
        print("4. Delete a todo item")
        print("5. Mark todo as complete")
        print("6. Mark todo as incomplete")
        print("7. Exit")
        print("========================")

    def get_user_choice(self):
        """
        Get the user's menu choice

        Returns:
            str: The user's choice
        """
        try:
            choice = input("Enter your choice (1-7): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nExiting application...")
            return "7"

    def add_todo(self):
        """
        Handle adding a new todo item
        """
        print("\n--- Add New Todo ---")
        title = input("Enter title: ").strip()

        if not title:
            print("Error: Title cannot be empty!")
            return

        description = input("Enter description (optional): ").strip()

        try:
            todo_id = self.service.add_todo(title, description)
            print(f"Todo item added successfully with ID: {todo_id}")
        except ValueError as e:
            print(f"Error: {e}")

    def view_todos(self):
        """
        Handle viewing all todo items
        """
        print("\n--- All Todo Items ---")
        todos = self.service.list_todos()

        if not todos:
            print("No todo items found.")
            return

        for todo in todos:
            status = "✓" if todo["completed"] else "○"
            print(f"[{status}] ID: {todo['id']}, Title: {todo['title']}")
            if todo["description"]:
                print(f"    Description: {todo['description']}")
            print()

    def update_todo(self):
        """
        Handle updating a todo item
        """
        print("\n--- Update Todo ---")
        try:
            todo_id = int(input("Enter the ID of the todo to update: "))
        except ValueError:
            print("Error: Please enter a valid ID number.")
            return

        # Check if todo exists
        try:
            existing_todo = self.service.get_todo(todo_id)
        except KeyError:
            print(f"Error: Todo with ID {todo_id} does not exist.")
            return

        print(f"Current title: {existing_todo['title']}")
        new_title = input("Enter new title (press Enter to keep current): ").strip()

        print(f"Current description: {existing_todo['description']}")
        new_description = input("Enter new description (press Enter to keep current): ").strip()

        # Prepare update parameters
        title_to_update = new_title if new_title else None
        description_to_update = new_description if new_description else None

        if title_to_update is None and description_to_update == "":
            # Special case: user wants to clear the description
            description_to_update = ""
        elif description_to_update == existing_todo['description']:
            # User didn't change the description
            description_to_update = None

        try:
            success = self.service.update_todo(todo_id, title=title_to_update, description=description_to_update)
            if success:
                print("Todo updated successfully.")
            else:
                print("Error: Todo could not be updated.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_todo(self):
        """
        Handle deleting a todo item
        """
        print("\n--- Delete Todo ---")
        try:
            todo_id = int(input("Enter the ID of the todo to delete: "))
        except ValueError:
            print("Error: Please enter a valid ID number.")
            return

        success = self.service.delete_todo(todo_id)
        if success:
            print("Todo deleted successfully.")
        else:
            print(f"Error: Todo with ID {todo_id} does not exist.")

    def mark_complete(self):
        """
        Handle marking a todo as complete
        """
        print("\n--- Mark Todo Complete ---")
        try:
            todo_id = int(input("Enter the ID of the todo to mark complete: "))
        except ValueError:
            print("Error: Please enter a valid ID number.")
            return

        success = self.service.mark_complete(todo_id)
        if success:
            print("Todo marked as complete.")
        else:
            print(f"Error: Todo with ID {todo_id} does not exist.")

    def mark_incomplete(self):
        """
        Handle marking a todo as incomplete
        """
        print("\n--- Mark Todo Incomplete ---")
        try:
            todo_id = int(input("Enter the ID of the todo to mark incomplete: "))
        except ValueError:
            print("Error: Please enter a valid ID number.")
            return

        success = self.service.mark_incomplete(todo_id)
        if success:
            print("Todo marked as incomplete.")
        else:
            print(f"Error: Todo with ID {todo_id} does not exist.")

    def run(self):
        """
        Main application loop
        """
        print("Welcome to the Todo Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_todo()
            elif choice == "2":
                self.view_todos()
            elif choice == "3":
                self.update_todo()
            elif choice == "4":
                self.delete_todo()
            elif choice == "5":
                self.mark_complete()
            elif choice == "6":
                self.mark_incomplete()
            elif choice == "7":
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-7.")

            # Pause to let user see the result before showing menu again
            input("\nPress Enter to continue...")


def main():
    """
    Main function to start the application
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()