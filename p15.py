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

    def find_lca(self, root, p, q):
        """Finds the Lowest Common Ancestor (LCA) in a BST."""
        if not root:
            return None

        # If both p and q are smaller than root, LCA lies in the left subtree
        if p < root.val and q < root.val:
            return self.find_lca(root.left, p, q)

        # If both p and q are greater than root, LCA lies in the right subtree
        elif p > root.val and q > root.val:
            return self.find_lca(root.right, p, q)

        # If p and q are on different sides, root is the LCA
        return root

# Example Usage
nums = [20, 10, 30, 5, 15, 25, 35]
bst = BST()
bst.build_bst(nums)

node1, node2 = 5, 15
lca_node = bst.find_lca(bst.root, node1, node2)

if lca_node:
    print(f"Lowest Common Ancestor of {node1} and {node2} is: {lca_node.val}")
else:
    print("Nodes not found in BST.")
