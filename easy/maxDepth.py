# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # if not root:
        #     return 0

        # deq = deque()
        # deq.append(root)
        # level = 0

        # while deq:
        #     level += 1
        #     for _ in range(len(deq)):
        #         d = deq.popleft()
        #         if d.left:
        #             deq.append(d.left)
        #         if d.right:
        #             deq.append(d.right)

        # return level

        depth = 0
        stack = [(root, 1)]

        while stack:
            node, d = stack.pop()
            if node:
                depth = max(depth, d)
                stack.append((node.left, d + 1))
                stack.append((node.right, d + 1))

        return depth


if __name__ == "__main__":
    # [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert Solution().maxDepth(root) == 3
