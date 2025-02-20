class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_mirror(tree1, tree2):
    """Checks if two trees are mirror images of each other."""
    if not tree1 and not tree2:
        return True  # Both trees are empty

    if not tree1 or not tree2:
        return False  # One tree is empty, and the other is not

    return (tree1.val == tree2.val and 
            is_mirror(tree1.left, tree2.right) and 
            is_mirror(tree1.right, tree2.left))

# Example Usage
def create_mirrored_trees():
    # Tree 1
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)

    # Tree 2 (Mirror of Tree 1)
    tree2 = TreeNode(1)
    tree2.left = TreeNode(3)
    tree2.right = TreeNode(2)
    tree2.right.left = TreeNode(5)
    tree2.right.right = TreeNode(4)

    return tree1, tree2

tree1, tree2 = create_mirrored_trees()
if is_mirror(tree1, tree2):
    print("The trees are mirror images of each other.")
else:
    print("The trees are NOT mirror images.")

