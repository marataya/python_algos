"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Recursive solution"""
        def has_sum(root, cur_sum):
            if root is None:
                return False

            cur_sum += root.val

            if not (root.left or root.right):
                return cur_sum == targetSum

            return has_sum(root.left, cur_sum) or has_sum(root.right, cur_sum)

        return has_sum(root, 0)

    def to_tree(arr):
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

if __name__ == '__main__':
    arr= [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root = Solution.to_tree(arr)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.left.val)
    print(root.left.right)
    print('>>>Tests:')
    print(Solution.hasPathSum(Solution, root, 22))

    arr = [1,2,3]
    root = Solution.to_tree(arr)
    print(Solution.hasPathSum(Solution, root, 5))
    print(Solution.hasPathSum(Solution, TreeNode(), 0))

