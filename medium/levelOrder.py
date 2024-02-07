# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res, queue = [], deque([root])

        while queue:
            level_values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_values)
        print(res)
        return res


if __name__ == "__main__":
    # Input: root = [3,9,20,null,null,15,7]
    # Output: [[3],[9,20],[15,7]]
    output = [[3], [9, 20], [15, 7]]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert Solution().levelOrder(root) == output
