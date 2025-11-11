"""
min_heap.py
-----------

A simple and efficient implementation of a Min Heap (priority queue) in Python.

Features:
- heappush: add element to the heap
- heappop: remove and return the smallest element
- heapify: maintain heap property after removal
- __len__, __repr__ support

Author: Mohsin Jafari
GitHub: https://github.com/mohsinjafari
"""

class MinHeap:
    """Min Heap implementation using a Python list as underlying storage."""

    def __init__(self):
        """Initialize an empty Min Heap."""
        self.heap = []

    # ----------------------------
    # Helper methods
    # ----------------------------
    def left(self, index):
        """Return the index of the left child of the given node index."""
        return 2 * index + 1

    def right(self, index):
        """Return the index of the right child of the given node index."""
        return 2 * index + 2

    def parent(self, index):
        """Return the index of the parent node of the given node index."""
        return (index - 1) // 2

    # ----------------------------
    # Core heap operations
    # ----------------------------
    def heappush(self, value):
        """Insert a new value into the heap."""
        self.heap.append(value)
        index = len(self.heap) - 1

        # Bubble up to maintain min-heap property
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = (
                self.heap[index],
                self.heap[self.parent(index)],
            )
            index = self.parent(index)

    def heappop(self):
        """Remove and return the smallest element from the heap."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return value

    def heapify(self, index):
        """Restore the min-heap property starting from the given index downward."""
        smallest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify(smallest)

    # ----------------------------
    # Magic methods
    # ----------------------------
    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return f"MinHeap({self.heap})"



# ----------------------------
# Example usage (for testing)
# ----------------------------
if __name__ == "__main__":
    h = MinHeap()
    data = [5, 3, 8, 1, 2, 9]

    print("MinHeap Demo\n-------------")
    print(f"Inserting values: {data}")
    for num in data:
        h.heappush(num)
    print(f"Heap after all insertions: {h}")

    print("\nPopping elements in ascending order:")
    while h:
        print(h.heappop(), end=" ")
    print()
