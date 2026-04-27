# linked_stack.py

# ================= NODE CLASS =================
class Node:
    def __init__(self, value):
        self.value = value      # store data
        self.next = None        # pointer to next node


# ================= STACK USING LINKED LIST =================
class LinkedStack:
    def __init__(self):
        self.top = None   # top of stack
        self.count = 0    # number of elements

    def push(self, value):
        # Create new node
        new_node = Node(value)

        # Point new node to current top
        new_node.next = self.top

        # Move top to new node
        self.top = new_node

        self.count += 1

    def pop(self):
        if self.is_empty():
            return None

        # Get top value
        removed_value = self.top.value

        # Move top to next node
        self.top = self.top.next

        self.count -= 1

        return removed_value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value 

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count 
    
    
    # ================= TEST =================
if __name__ == "__main__":
    stack = LinkedStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top:", stack.peek())     # 30
    print("Popped:", stack.pop())   # 30
    print("Size:", stack.size())    # 2