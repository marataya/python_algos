"""
113. Path Sum II
Medium
Topics -- Backtracking -- Tree -- Depth-First Search -- Binary Tree

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

"""
from typing import Optional, List

from tree.leetcode.tree_utils import TreeNode, To_tree


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(root: TreeNode, targetSum: int, path: List[int]):
            if root is None:
                return
            if root.left is None and root.right is None: # base case of recursion when node is a leaf
                if root.val == targetSum: # checking if targetSum
                    result.append(path + [root.val])
                    return
            dfs(root.left, targetSum - root.val, path + [root.val])
            dfs(root.right, targetSum - root.val, path + [root.val])

        dfs(root, targetSum, [])
        return result


if __name__ == '__main__':
    arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    root = To_tree(arr)
    print(Solution.pathSum(Solution, root, 22))
