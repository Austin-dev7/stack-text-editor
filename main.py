# main.py

from stack import Stack

# Create stacks
undo_stack = Stack()   # Stores previous states (for undo)
redo_stack = Stack()   # Stores undone states (for redo)

# Current text in editor
current_text = ""


# ================= TEXT FUNCTIONS =================

def type_text(new_text):
    global current_text, redo_stack

    # Save current state before making changes (for undo feature)
    undo_stack.push(current_text)

    # Add space if text already exists, then append new text
    if current_text:
        current_text += " " + new_text
    else:
        current_text = new_text

    # Clear redo stack because new action cancels redo history
    redo_stack = Stack()

    # Display updated text
    print("Text:", current_text)


def undo():
    global current_text

    # Check if there is something to undo
    if not undo_stack.is_empty():
        # Save current state into redo stack
        redo_stack.push(current_text)

        # Restore last saved state
        current_text = undo_stack.pop()
    else:
        print("Nothing to undo")

    # Display updated text
    print("Text:", current_text)


def redo():
    global current_text

    # Check if there is something to redo
    if not redo_stack.is_empty():
        # Save current state into undo stack
        undo_stack.push(current_text)

        # Restore last undone state
        current_text = redo_stack.pop()
    else:
        print("Nothing to redo")

    # Display updated text
    print("Text:", current_text)


# ================= FILE FEATURES =================

def save_to_file():
    global current_text

    # Ask user for filename
    filename = input("Enter filename (e.g. file.txt): ")

    try:
        # Open file in write mode and save text
        with open(filename, "w") as file:
            file.write(current_text)

        print("File saved successfully")

    except Exception as e:
        print("Error saving file:", e)


def load_from_file():
    global current_text

    # Ask user for filename
    filename = input("Enter filename to load: ")

    try:
        # Open file in read mode and load content
        with open(filename, "r") as file:
            current_text = file.read()

        print("File loaded successfully")
        print("Text:", current_text)

    except Exception as e:
        print("Error loading file:", e)


def clear_text():
    global current_text

    # Save current state so we can undo the clear action
    undo_stack.push(current_text)

    # Clear the text
    current_text = ""

    print("Text cleared")


def search_word():
    global current_text

    # Ask user for word to search
    word = input("Enter word to search: ")

    # Check if word exists in text
    if word in current_text:
        print(f"'{word}' found in text ")
    else:
        print(f"'{word}' not found ")


# ================= MENU =================

def menu():
    while True:
        # Display menu options
        print("\n--- TEXT EDITOR ---")
        print("1. Type Text")
        print("2. Undo")
        print("3. Redo")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Clear Text")
        print("7. Search Word")
        print("8. Exit")

        # Get user input
        choice = input("Choose: ")

        if choice == "1":
            # Get new text and add it
            new_text = input("Enter text: ")
            type_text(new_text)

        elif choice == "2":
            # Undo last action
            undo()

        elif choice == "3":
            # Redo last undone action
            redo()

        elif choice == "4":
            # Save text to file
            save_to_file()

        elif choice == "5":
            # Load text from file
            load_from_file()

        elif choice == "6":
            # Clear all text
            clear_text()

        elif choice == "7":
            # Search for a word
            search_word()

        elif choice == "8":
            # Exit program
            print("Goodbye")
            break

        else:
            # Handle invalid input
            print("Invalid choice")


# Run the program
menu()