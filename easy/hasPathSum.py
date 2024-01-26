# https://leetcode.com/problems/path-sum/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], cur_sum: int):
            if not node:
                return False

            cur_sum += node.val
            if not node.left and not node.right:
                return cur_sum == targetSum

            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

        return dfs(root, 0)


if __name__ == "__main__":
    # root = [5,4,8,11,null,13,4,7,2,null,null,null,1],
    targetSum = 22
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)

    assert Solution().hasPathSum(root, targetSum) == True
