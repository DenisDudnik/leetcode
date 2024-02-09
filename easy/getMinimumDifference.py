# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        node, stack, values = root, [], []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.val)
            node = node.right
            if len(values) > 1:
                min_diff = min(min_diff, abs(values[-1] - values[-2]))
                if min_diff == 1:
                    return min_diff

        return min_diff


if __name__ == "__main__":
    # Input: root = [4,2,6,1,3]
    # Output: 1
    output = 1
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    assert Solution().getMinimumDifference(root) == output

    # Input: root = [236,104,701,null,227,null,911]
    # Output: 9
    output = 9
    root = TreeNode(236)
    root.left = TreeNode(104)
    root.right = TreeNode(701)
    root.left.right = TreeNode(227)
    root.right.right = TreeNode(911)

    assert Solution().getMinimumDifference(root) == output
