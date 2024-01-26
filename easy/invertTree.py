# https://leetcode.com/problems/invert-binary-tree/

from collections import deque
from typing import Optional

from isSameTree import Solution as equal


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deq = deque()
        deq.append(root)

        while deq:
            for _ in range(len(deq)):
                node = deq.popleft()
                if node:
                    node.left, node.right = node.right, node.left
                    deq.append(node.left)
                    deq.append(node.right)

        return root


if __name__ == "__main__":
    # root = [4,2,7,1,3,6,9], res = [4,7,2,9,6,3,1]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    res = TreeNode(4)
    res.left = TreeNode(7)
    res.right = TreeNode(2)
    res.left.left = TreeNode(9)
    res.left.right = TreeNode(6)
    res.right.left = TreeNode(3)
    res.right.right = TreeNode(1)

    r = Solution().invertTree(root)

    assert equal().isSameTree(res, r) == True

    # root = [2,1,3], res = [2,3,1]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    res = TreeNode(2)
    res.left = TreeNode(3)
    res.right = TreeNode(1)

    r = Solution().invertTree(root)

    assert equal().isSameTree(res, r) == True

    # root = [], res = []
    root = None

    res = None

    r = Solution().invertTree(root)

    assert equal().isSameTree(res, r) == True
