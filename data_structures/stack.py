"""
stack.py
---------
A simple and efficient implementation of a Stack (LIFO) in Python.

Features:
- push: add element to top
- pop: remove element from top
- peek: view top element without removing
- is_empty: check if stack is empty
- size: return number of elements
- clear: remove all elements
- __iter__, __len__, and __repr__ support
"""

class Node:
    """A node in a stack."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """Stack implementation using Python list as underlying storage."""



    def __init__(self):
        self.head = None
        self.length = 0


    # ----------------------------
    # Basic operations
    # ----------------------------
    def push(self, data):
        """Add element to the top of the stack."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node    
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    

    def pop(self):
        """Remove and return the top item from the stack. Returns None if stack is empty."""
        if self.head == None:
            return None
        val = self.head.data
        self.head = self.head.next  
        self.length -= 1
        return val
    


    def peek(self):
        """Return the top item from the stack without removing it. Returns None if stack is empty."""
        if self.head == None:
            return None
        return self.head.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.length == 0

    def clear(self):
        """Remove all items from the stack."""
        self.head = None
        self.length = 0



    # ----------------------------
    # Magic methods
    # ----------------------------

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return "Stack([" + ", ".join(reversed(items)) + "])"


# ----------------------------
# Example usage (for testing)
# ----------------------------
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)            # Stack([10, 20, 30])
    print(stack.peek())     # 30
    print(stack.pop())      # 30
    print(len(stack))       # 2
    print(stack.is_empty()) # False
    stack.clear()
    print(stack.is_empty()) # True
