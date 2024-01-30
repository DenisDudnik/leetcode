# https://leetcode.com/problems/count-complete-tree-nodes/

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        count = 1

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                count += 1
            else:
                return count
            if node.right:
                queue.append(node.right)
                count += 1
            else:
                return count


if __name__ == "__main__":
    # Input: root = [1,2,3,4,5,6]
    # Output: 6
    output = 6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    assert Solution().countNodes(root) == output
