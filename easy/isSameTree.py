# https://leetcode.com/problems/same-tree/

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        deq_p, deq_q = deque(), deque()
        deq_p.append(p)
        deq_q.append(q)
        while deq_p and deq_q:
            if not len(deq_p) == len(deq_q):
                return False
            for _ in range(len(deq_p)):
                node_p = deq_p.popleft()
                node_q = deq_q.popleft()

                if node_p:
                    node_p_val = node_p.val
                    deq_p.append(node_p.left)
                    deq_p.append(node_p.right)
                else:
                    node_p_val = None

                if node_q:
                    node_q_val = node_q.val
                    deq_q.append(node_q.left)
                    deq_q.append(node_q.right)
                else:
                    node_q_val = None

                if not node_p_val == node_q_val:
                    return False
        return True


if __name__ == "__main__":
    # p = [1,2,3] q = [1,2,3]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    assert Solution().isSameTree(p, q) == True

    # p = [1,2], q = [1,null,2]
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.left = None
    q.right = TreeNode(2)

    assert Solution().isSameTree(p, q) == False

    # p = [1,2,1], q = [1,1,2]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)

    assert Solution().isSameTree(p, q) == False
