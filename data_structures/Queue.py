"""Implementation of a Queue data structure using a doubly linked list in Python."""

class Node:
    """A node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    """A Queue data structure implemented using a doubly linked list."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    
    "Basic operations"
    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node   
            self.head = new_node
        self.length += 1
    
    def dequeue(self):
        if self.head == None:
            return None
        else:
            val = self.tail.data
            self.tail = self.tail.prev
            if self.tail == None:
                self.head = None
            else:
                self.tail.next = None   
            self.length -= 1
            return val
    

    def is_empty(self):
            return self.length == 0
    
    "magic methods"
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __len__(self):
        return self.length


    def __repr__(self):
        items = []
        temp = self.head
        while temp:
            items.append(repr(temp.data))
            temp = temp.next
        return "Queue(" + ", ".join(items) + ")"
    


"Testing the Queue implementation"

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)  # Queue(3, 2, 1)
    print(q.dequeue())  # 1
    print(q)  # Queue(3, 2)
    print(len(q))  # 2
    print(q.is_empty())  # False
    q.dequeue()
    q.dequeue()
    print(q.is_empty())  # True
