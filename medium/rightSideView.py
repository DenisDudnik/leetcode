# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res, queue = [], deque([root])
        while queue:
            val = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    val = node.val
            if val is not None:
                res.append(val)
        print(res)
        return res


if __name__ == "__main__":
    # Input: root = [1,2,3,null,5,null,4]
    # Output: [1,3,4]
    output = [1, 3, 4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    assert Solution().rightSideView(root) == output

    # Input: root = [1,2,3,4]
    # Output: [1,3,4]
    output = [1, 3, 4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    assert Solution().rightSideView(root) == output
