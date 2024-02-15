# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node, stack, next_node = root, [], None
        while node:
            if node.right:
                stack.append(node.right)
            next_node = node.left
            if not next_node and stack:
                next_node = stack.pop()
            node.right = next_node
            node.left = None
            node = next_node


if __name__ == "__main__":
    # Input: root = [1,2,5,3,4,null,6]
    # Output: [1,null,2,null,3,null,4,null,5,null,6]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    output = TreeNode(1)
    output.right = TreeNode(2)
    output.right.right = TreeNode(3)
    output.right.right.right = TreeNode(4)
    output.right.right.right.right = TreeNode(5)
    output.right.right.right.right.right = TreeNode(6)

    Solution().flatten(root)
    assert root == output
