# browser.py

from stack import Stack

# Create stacks
back_stack = Stack()      # stores previous pages
forward_stack = Stack()   # stores forward pages

# Current page
current_page = "Home"


# ================= FUNCTIONS =================

def visit_page(url):
    global current_page, forward_stack

    # Save current page before visiting new one
    back_stack.push(current_page)

    # Update current page
    current_page = url

    # Clear forward history
    forward_stack = Stack()

    print("Current page:", current_page)


def go_back():
    global current_page

    if not back_stack.is_empty():
        # Save current page to forward stack
        forward_stack.push(current_page)

        # Go back to previous page
        current_page = back_stack.pop()
    else:
        print("No pages to go back")

    print("Current page:", current_page)


def go_forward():
    global current_page

    if not forward_stack.is_empty():
        # Save current page to back stack
        back_stack.push(current_page)

        # Move forward
        current_page = forward_stack.pop()
    else:
        print("No pages to go forward")

    print("Current page:", current_page)


# ================= MENU =================

def menu():
    while True:
        print("\n--- BROWSER ---")
        print("1. Visit Page")
        print("2. Back")
        print("3. Forward")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            url = input("Enter website: ")
            visit_page(url)

        elif choice == "2":
            go_back()

        elif choice == "3":
            go_forward()

        elif choice == "4":
            print("Exiting browser 👋")
            break

        else:
            print("Invalid choice")


# Run program
menu()