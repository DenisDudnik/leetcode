# https://leetcode.com/problems/symmetric-tree/

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        deq_l, deq_r = deque(), deque()
        deq_l.append(root.left)
        deq_r.append(root.right)

        while deq_l and deq_r:
            if not len(deq_l) == len(deq_r):
                return False
            for _ in range(len(deq_l)):
                node_l = deq_l.popleft()
                node_r = deq_r.pop()
                if node_l:
                    deq_l.append(node_l.left)
                    deq_l.append(node_l.right)
                    node_l_val = node_l.val
                else:
                    node_l_val = None
                if node_r:
                    deq_r.appendleft(node_r.right)
                    deq_r.appendleft(node_r.left)
                    node_r_val = node_r.val
                else:
                    node_r_val = None

                if not node_l_val == node_r_val:
                    return False

        return True


if __name__ == "__main__":
    # root = [1,2,2,3,4,4,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    assert Solution().isSymmetric(root) == True

    # root = [1,2,2,null,3,null,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(None)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(None)
    root.right.right = TreeNode(3)

    assert Solution().isSymmetric(root) == False
