"""
searching_algorithms.py
------------------------
Implement common search algorithms in Python including:
- Linear Search
- Binary Search (for sorted lists)

Author: Mohsin Jafari
GitHub: https://github.com/mohsinjafari
"""

# ----------------------------
# Linear Search
# ----------------------------
def linear_search(arr, target):
    """
    Perform a linear search on the given array to find the target value.

    Parameters:
    arr (list): The list of elements to search through.
    target: The value to search for in the list.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


# ----------------------------
# Binary Search
# ----------------------------
def binary_search(arr, target):
    """
    Perform a binary search on the given sorted array to find the target value.

    Parameters:
    arr (list): The sorted list of elements to search through.
    target: The value to search for in the list.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]

    print("Original array:", arr)
    print("Linear search for 7:", linear_search(arr, 7))
    print("Linear search for 4:", linear_search(arr, 4))
    print("Binary search for 7:", binary_search(arr, 7))
    print("Binary search for 4:", binary_search(arr, 4))
