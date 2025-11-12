"""
priority_queue.py
-----------------
A simple and efficient implementation of a Priority Queue in Python.

Features:
- append: add an item with a priority
- pop: remove and return the item with the highest priority (lowest number)
- peek: view the priority of the highest-priority item without removing
- is_empty: check if the queue is empty
- __repr__: display the queue's items

Author: Mohsin Jafari
GitHub: https://github.com/mohsinjafari
"""


class PriorityQueue:
    """A simple priority queue implementation where lower priority numbers come first."""

    def __init__(self):
        self.queue = []

    def append(self, priority, item):
        """Add an item with its priority to the queue."""
        self.queue.append((priority, item))
        self.queue.sort(key=lambda x: x[0])  # Sort by priority

    def pop(self):
        """Remove and return the item with the highest priority (lowest number)."""
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        return self.queue.pop(0)[1]

    def peek(self):
        """Return the item with the highest priority without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self.queue[0][1]

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.queue) == 0

    def __repr__(self):
        """Return a string representation of the items in the queue."""
        return str([item for _, item in self.queue])
