# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node, stack = root, []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right


if __name__ == "__main__":
    # Input: root = [3,1,4,null,2], k = 1
    # Output: 1
    k = 1
    output = 1
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    assert Solution().kthSmallest(root, k) == output
