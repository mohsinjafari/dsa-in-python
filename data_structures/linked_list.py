"""
linked_list.py
----------------
A simple and efficient implementation of a Singly Linked List in Python.

Features:
- Append (to right and left)
- Insert at index
- Pop by index
- Reverse the list
- Detect cycles (Floyd's algorithm and visited-set method)
- Find value index
- Clear and check empty
- Iterable, indexable, comparable
- Convert to Python list
"""

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None



class Linked_List:
    """Singly Linked List implementation."""
    def __init__(self):
        self.head = None
        self.length = 0

    # ----------------------------
    # Basic operations
    # ----------------------------

    def append_left(self, data):
        """Add element to the beginning of the list."""
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    
    
    def append(self, data):
        """Add element to the end of the list."""
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            
            temp.next = new_node
        self.length += 1


    

    def insert(self, index, data):
        """Insert element at a given index."""

        if index < 0 or index >= self.length:
            raise IndexError()
        elif index == 0:
            self.append_left(data)
        
        else:
            new_node = Node(data)
            f, s= self.head, self.head.next
            while index > 1:
                f = s
                s = s.next
                index -= 1
            new_node.next = s
            f.next = new_node
        self.length += 1


    def pop(self, index):
        """Remove and return element at given index."""
        if index < 0 or index >= self.length:
            raise IndexError()

        elif index == 0:
            val = self.head.data
            self.head = self.head.next
        
        else:
            f,s = self.head, self.head.next
            while index > 1:
                f = s
                s = s.next
                index -= 1
            
            val = s.data
            f.next = s.next
        self.length-=1 
        return val

    def is_empty(self):
        """Check if list is empty."""
        return self.length == 0
    

    
    def clear(self):
        """Remove all elements from the list."""
        self.head = None
        self.length = 0






    # ----------------------------
    # Utility methods
    # ----------------------------

    def find(self, value):
        """Return index of first occurrence of value, or -1 if not found."""
        temp = self.head
        index = 0
        while temp:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1
        return -1

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def floyd_cycle(self):
        """Detect a cycle using Floyd's cycle detection algorithm."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def has_loop(self):
        """Detect a cycle using a visited set."""
        visited = set()
        temp = self.head
        while temp:
            if temp not in visited:
                visited.add(temp)
                temp = temp.next
            else:
                return True
        return False

    def to_list(self):
        """Convert linked list to a Python list."""
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

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


    def __eq__(self, other):
        if not isinstance(other, Linked_List):
            return False
        a, b = self.head, other.head
        while a and b:
            if a.data != b.data:
                return False
            a, b = a.next, b.next
        return a is None and b is None

    def __repr__(self):
        values = []
        temp = self.head
        while temp:
            values.append(str(temp.data))
            temp = temp.next
        return "Linked_List([" + " -> ".join(values) + "])"
    

# ----------------------------
# Example usage (for testing)
# ----------------------------
if __name__ == "__main__":
    ll = Linked_List()
    ll.append(10)
    ll.append(20)
    ll.append_left(5)
    ll.insert(2, 15)
    print(ll)
    print("List length:", len(ll))
    print("Index of 20:", ll.find(20))
    ll.reverse()
    print("Reversed:", ll)
    print("To list:", ll.to_list())