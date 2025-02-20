class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True

    if not (min_val < root.val < max_val):
        return False

    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))

# Example Usage
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_valid_bst(root))  # Output: True
