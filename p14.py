class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        """Recursively inserts a value into the BST."""
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def build_bst(self, nums):
        """Builds a BST from a list of numbers."""
        for num in nums:
            self.root = self.insert(self.root, num)

    def left_boundary(self, root):
        """Prints the left boundary (excluding leaf nodes)."""
        if root:
            if root.left:
                print(root.val, end=" ")
                self.left_boundary(root.left)
            elif root.right:
                print(root.val, end=" ")
                self.left_boundary(root.right)

    def right_boundary(self, root):
        """Prints the right boundary (excluding leaf nodes, in reverse)."""
        if root:
            if root.right:
                self.right_boundary(root.right)
                print(root.val, end=" ")
            elif root.left:
                self.right_boundary(root.left)
                print(root.val, end=" ")

    def leaf_nodes(self, root):
        """Prints the leaf nodes from left to right."""
        if root:
            self.leaf_nodes(root.left)
            if root.left is None and root.right is None:
                print(root.val, end=" ")
            self.leaf_nodes(root.right)

    def boundary_traversal(self, root):
        """Performs boundary traversal of the BST."""
        if not root:
            return

        print(root.val, end=" ")  # Print root first

        # Left boundary (excluding root and leaves)
        self.left_boundary(root.left)

        # Leaf nodes
        self.leaf_nodes(root.left)
        self.leaf_nodes(root.right)

        # Right boundary (excluding root and leaves, printed in reverse)
        self.right_boundary(root.right)

# Example Usage
nums = [10, 5, 15, 3, 7, 13, 18]
bst = BST()
bst.build_bst(nums)

print("Boundary Traversal of BST:")
bst.boundary_traversal(bst.root)
