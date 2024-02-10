class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def To_tree(arr):
    """
    Converts an array-based binary tree to a class-based binary tree.

    Args:
      arr: An array representing the binary tree.

    Returns:
      The root node of the class-based binary tree.
    """

    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while queue and i < len(arr):
        node = queue.pop(0)

        if arr[i]:
            node.left = TreeNode(arr[i])
            queue.append(node.left)

        i += 1

        if i < len(arr) and arr[i]:
            node.right = TreeNode(arr[i])
            queue.append(node.right)

        i += 1

    return root
