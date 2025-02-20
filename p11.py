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

    def inorder_traversal(self, root):
        """Performs an inorder traversal (sorted order)."""
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

# Example Usage
nums = [10, 5, 15, 3, 7, 13, 18]  # Example input
bst = BST()
bst.build_bst(nums)

print("Inorder Traversal of BST (Sorted Order):")
bst.inorder_traversal(bst.root)
