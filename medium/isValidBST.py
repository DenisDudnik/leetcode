# https://leetcode.com/problems/validate-binary-search-tree/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node, stack, value = root, [], float("-inf")

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= value:
                return False
            value = node.val
            node = node.right

        return True


if __name__ == "__main__":
    # Input: root = [2,1,3]
    # Output: true
    output = True
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    assert Solution().isValidBST(root) == output

    # Input: root = [5,4,6,null,null,3,7]
    # Output: false
    output = False
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)

    assert Solution().isValidBST(root) == output
