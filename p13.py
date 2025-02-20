class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        """Recursively inserts a value into the tree (BST insertion for simplicity)."""
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def build_tree(self, nums):
        """Builds a Binary Search Tree from a list of numbers."""
        for num in nums:
            self.root = self.insert(self.root, num)

    def inorder_traversal(self, root):
        """Inorder Traversal: Left -> Root -> Right"""
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        """Preorder Traversal: Root -> Left -> Right"""
        if root:
            print(root.val, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        """Postorder Traversal: Left -> Right -> Root"""
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val, end=" ")

# Example Usage
nums = [10, 5, 15, 3, 7, 13, 18]
tree = BinaryTree()
tree.build_tree(nums)

print("\nInorder Traversal (Sorted Order):")
tree.inorder_traversal(tree.root)

print("\nPreorder Traversal:")
tree.preorder_traversal(tree.root)

print("\nPostorder Traversal:")
tree.postorder_traversal(tree.root)
