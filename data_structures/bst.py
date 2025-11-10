"""
bst.py
----------------
A simple and efficient implementation of a Binary Search Tree (BST) in Python.

Features:
- Add child (insert new nodes)
- Inorder, Preorder, Postorder traversals
- Reverse BST
- Search for a value
- Compute tree height
- Find maximum and minimum values
- Build BST from a list

Author: Mohsin Jafari
GitHub: https://github.com/mohsinjafari
"""

# ========================================
# Binary Search Tree (BST) Implementation
# ========================================

class BSTNode:
    """
    A class representing a node in a Binary Search Tree (BST).
    Each node contains a data value and references to left and right children.
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # -------------------------------
    # Insert a new node (add_child)
    # -------------------------------
    def add_child(self, data):
        """
        Adds a new node to the BST in the correct position.
        Duplicate values are ignored (no duplicates allowed in BST).
        """
        if data == self.data:
            return  # Ignore duplicate

        if data < self.data:
            # Insert into left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            # Insert into right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

    # -------------------------------
    # Inorder Traversal (LNR)
    # -------------------------------
    def inorder_traversal(self):
        """
        Returns elements in ascending order (Left → Node → Right).
        """
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    # -------------------------------
    # Preorder Traversal (NLR)
    # -------------------------------
    def preorder_traversal(self):
        """
        Returns elements in preorder (Node → Left → Right).
        """
        elements = [self.data]

        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    # -------------------------------
    # Postorder Traversal (LRN)
    # -------------------------------
    def postorder_traversal(self):
        """
        Returns elements in postorder (Left → Right → Node).
        """
        elements = []

        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)
        return elements

    # -------------------------------
    # Reverse BST
    # -------------------------------
    def reverse(self):
        """
        reverses the BST by swapping left and right children recursively.
        """
        self.left, self.right = self.right, self.left  # Swap children
        if self.left:
            self.left.reverse()
        if self.right:
            self.right.reverse()

    # -------------------------------
    # Search for a value
    # -------------------------------
    def search(self, value):
        """
        Returns True if value exists in the BST, otherwise False.
        """
        if value == self.data:
            return True

        if value < self.data:
            return self.left.search(value) if self.left else False
        else:
            return self.right.search(value) if self.right else False

    # -------------------------------
    # Find the height of the tree
    # -------------------------------
    def height(self):
        """
        Returns the height (maximum depth) of the BST.
        """
        max_height = 0
        if self.left:
            max_height = max(max_height, self.left.height())
        if self.right:
            max_height = max(max_height, self.right.height())
        return max_height + 1

    # -------------------------------
    # Find the maximum value in the tree
    # -------------------------------
    def max_val(self):
        """
        Returns the maximum value stored in the BST.
        """
        current = self
        while current.right:
            current = current.right 
        return current.data

    # -------------------------------
    # Find the minimum value in the tree
    # -------------------------------
    def min_val(self):
        """
        Returns the minimum value stored in the BST.
        """
        current = self
        while current.left:
            current = current.left 
        return current.data


# ========================================
# Helper Function to Build a BST
# ========================================
def build_tree(elements):
    """
    Creates a BST from a list of elements.
    """
    if not elements:
        return None

    root = BSTNode(elements[0])
    for elem in elements[1:]:
        root.add_child(elem)
    return root


# ========================================
# Example Usage (Uncomment to Test)
# ========================================
if __name__ == "__main__":
    numbers = [15, 12, 27, 7, 14, 20, 88, 23]
    bst = build_tree(numbers)

    print("Inorder Traversal:", bst.inorder_traversal())
    print("Preorder Traversal:", bst.preorder_traversal())
    print("Postorder Traversal:", bst.postorder_traversal())
    print("Reverse Inorder:", bst.reverse_inorder())
    print("Search 20:", bst.search(20))
    print("Search 99:", bst.search(99))
    print("Height:", bst.height())
    print("Max Value:", bst.max_val())
    print("Min Value:", bst.min_val())
