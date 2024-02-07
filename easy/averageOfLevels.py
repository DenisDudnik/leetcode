# https://leetcode.com/problems/average-of-levels-in-binary-tree/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res, queue = [], deque([root])

        while queue:
            level_sum, level_count = 0, len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_sum += node.val
            res.append(level_sum / level_count)

        print(res)
        return res


if __name__ == "__main__":
    # Input: root = [3,9,20,null,null,15,7]
    # Output: [3.00000,14.50000,11.00000]
    output = [3, 14.5, 11]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert Solution().averageOfLevels(root) == output
