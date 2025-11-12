"""
heapq_demo.py
-------------
Efficient demonstration of min-heap and priority queue using Python's heapq module.

Features:
- Min-Heap: transform a list into a heap and pop elements in ascending order
- Priority Queue: process tasks by priority
- Uses heapify for efficient heap creation

Author: Mohsin Jafari
GitHub: https://github.com/mohsinjafari
"""

import heapq

# -------------------------------
# Min-Heap example
# -------------------------------
numbers = [5, 7, 9, 1, 3]

# Transform list into a min-heap in-place
heapq.heapify(numbers)
print("Min Heap:", numbers)

# Pop all elements in sorted order
print("Sorted elements:", end=" ")
while numbers:
    print(heapq.heappop(numbers), end=" ")
print("\n")

# -------------------------------
# Priority Queue example
# -------------------------------
tasks = [(1, "task1"), (3, "task3"), (2, "task2")]

# Transform list of tasks into a heap
heapq.heapify(tasks)

print("Processing tasks by priority:")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Task: {task}, Priority: {priority}")
