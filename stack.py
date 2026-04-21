# stack.py

class Stack:
    def __init__(self):
        # This list will store all stack elements
        self.items = []

    def push(self, value):
        # Add a new item to the top of the stack
        self.items.append(value)

    def pop(self):
        # Remove and return the top item from the stack
        if not self.is_empty():
            return self.items.pop()
        return None  # Return None if stack is empty

    def peek(self):
        # Return the top item without removing it
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        # Check if the stack has no elements
        return len(self.items) == 0

    def size(self):
        # Return the number of elements in the stack
        return len(self.items)