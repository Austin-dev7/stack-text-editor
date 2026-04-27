# main.py

from stack import Stack

# Create stacks
undo_stack = Stack()
redo_stack = Stack()

# Current text in editor
current_text = ""


# ================= TEXT FUNCTIONS =================

def type_text(new_text):
    global current_text, redo_stack

    # Save current state for undo
    undo_stack.push(current_text)

    # Add space if needed
    if current_text:
        current_text += " " + new_text
    else:
        current_text = new_text

    # Clear redo stack
    redo_stack = Stack()

    print("Text:", current_text)


def undo():
    global current_text

    if not undo_stack.is_empty():
        redo_stack.push(current_text)
        current_text = undo_stack.pop()
    else:
        print("Nothing to undo")

    print("Text:", current_text)


def redo():
    global current_text

    if not redo_stack.is_empty():
        undo_stack.push(current_text)
        current_text = redo_stack.pop()
    else:
        print("Nothing to redo")

    print("Text:", current_text)


# ================= FILE FEATURES =================

def save_to_file():
    global current_text

    filename = input("Enter filename (e.g. file.txt): ")

    try:
        with open(filename, "w") as file:
            file.write(current_text)

        print("File saved successfully")

    except Exception as e:
        print("Error saving file:", e)


def load_from_file():
    global current_text

    filename = input("Enter filename to load: ")

    try:
        with open(filename, "r") as file:
            current_text = file.read()

        print("File loaded successfully")
        print("Text:", current_text)

    except Exception as e:
        print("Error loading file:", e)


def clear_text():
    global current_text

    undo_stack.push(current_text)  # allow undo
    current_text = ""

    print("Text cleared")


def search_word():
    global current_text

    word = input("Enter word to search: ")

    if word in current_text:
        print(f"'{word}' found in text ")
    else:
        print(f"'{word}' not found ❌")


# ================= MENU =================

def menu():
    while True:
        print("\n--- TEXT EDITOR ---")
        print("1. Type Text")
        print("2. Undo")
        print("3. Redo")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Clear Text")
        print("7. Search Word")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == "1":
            new_text = input("Enter text: ")
            type_text(new_text)

        elif choice == "2":
            undo()

        elif choice == "3":
            redo()

        elif choice == "4":
            save_to_file()

        elif choice == "5":
            load_from_file()

        elif choice == "6":
            clear_text()

        elif choice == "7":
            search_word()

        elif choice == "8":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


# Run program
menu()