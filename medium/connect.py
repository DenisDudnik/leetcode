# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        queue = deque([root])

        while queue:
            level_count = len(queue)
            for i in range(level_count):
                node = queue.popleft()
                if i < level_count - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


if __name__ == "__main__":
    # Input: root = [1,2,3,4,5,null,7]
    # Output: [1,#,2,3,#,4,5,7,#]
    # Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point
    # to its next right node, just like in Figure B. The serialized output is in level order as connected by the next
    # pointers, with '#' signifying the end of each level.

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)

    output = Node(1)
    output.left = Node(2)
    output.right = Node(3)
    output.left.left = Node(4)
    output.left.right = Node(5)
    output.right.right = Node(7)

    output.left.next = output.right
    output.left.left.next = output.left.right
    output.left.right.next = output.right.right

    # this assert doesn't work, but code is working
    assert Solution().connect(root) == output
