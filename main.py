# main.py 

from stack import Stack

# Create two stacks:
# undo_stack → stores previous states
# redo_stack → stores undone states
undo_stack = Stack()
redo_stack = Stack()

# This holds the current text in the editor
current_text = ""


def type_text(new_text):
    global current_text, redo_stack

    # Save current state BEFORE making changes (for undo)
    undo_stack.push(current_text)

    # Add space only if text already exists, then add new text
    if current_text:
        current_text += " " + new_text
    else:
        current_text = new_text

    # Clear redo history because new action invalidates redo
    redo_stack = Stack()

    # Show updated text
    print("Text:", current_text)


def undo():
    global current_text

    # Check if there is something to undo
    if not undo_stack.is_empty():
        # Save current state to redo stack
        redo_stack.push(current_text)

        # Restore previous state
        current_text = undo_stack.pop()
    else:
        print("Nothing to undo")

    # Show updated text
    print("Text:", current_text)


def redo():
    global current_text

    # Check if there is something to redo
    if not redo_stack.is_empty():
        # Save current state to undo stack
        undo_stack.push(current_text)

        # Restore last undone state
        current_text = redo_stack.pop()
    else:
        print("Nothing to redo")

    # Show updated text
    print("Text:", current_text)


# ================= USER MENU =================

def menu():
    while True:
        # Display menu options
        print("\n--- TEXT EDITOR ---")
        print("1. Type Text")
        print("2. Undo")
        print("3. Redo")
        print("4. Exit")

        # Get user choice
        choice = input("Choose: ")

        if choice == "1":
            # Ask user for new text input
            new_text = input("Enter text: ")

            # Call function to update text
            type_text(new_text)

        elif choice == "2":
            # Undo last action
            undo()

        elif choice == "3":
            # Redo last undone action
            redo()

        elif choice == "4":
            # Exit program
            print("Goodbye 👋")
            break

        else:
            # Handle invalid input
            print("Invalid choice")


# Start the program
menu()