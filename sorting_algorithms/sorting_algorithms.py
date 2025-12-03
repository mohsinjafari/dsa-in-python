"""
sorting_algorithms.py
------------------------
Implement common sorting algorithms in Python including:
- Selection Sort
- Insertion Sort
- Bubble Sort
- Merge Sort

Author: Mohsin Jafari
GitHub: https://github.com/mohsinjafari
"""

# ----------------------------
# Selection Sort
# ----------------------------
def selection_sort(arr):
    """
    Sort the list using Selection Sort algorithm.
    At each step, select the smallest element from the unsorted part
    and swap it with the first unsorted element.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# ----------------------------
# Insertion Sort
# ----------------------------
def insertion_sort(arr):
    """
    Sort the list using Insertion Sort algorithm.
    Insert each element into its correct position in the sorted part.
    """
    n = len(arr)
    for i in range(1, n):
        for j in range(i):
            if arr[i] < arr[j]:
                temp = arr[i]
                del arr[i]
                arr.insert(j, temp)
                break
    return arr


# ----------------------------
# Bubble Sort
# ----------------------------
def bubble_sort(arr):
    """
    Sort the list using Bubble Sort algorithm.
    Repeatedly swap adjacent elements if they are in the wrong order.
    Optimized to stop early if no swaps occur in a pass.
    """
    n = len(arr)
    for i in range(n - 1):
        flag = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break
    return arr


# ----------------------------
# Merge Helper Function
# ----------------------------
def merge(lst1, lst2):
    """
    Merge two sorted lists into a single sorted list.
    """
    i, j = 0, 0
    result = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    result += lst1[i:]
    result += lst2[j:]
    return result


# ----------------------------
# Merge Sort
# ----------------------------
def merge_sort(arr):
    """
    Sort the list using Merge Sort algorithm.
    Divide the list into halves, recursively sort each half, and merge.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]

    print("Original array:", arr)
    print("Selection Sort:", selection_sort(arr.copy()))
    print("Insertion Sort:", insertion_sort(arr.copy()))
    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Merge Sort:", merge_sort(arr.copy()))
