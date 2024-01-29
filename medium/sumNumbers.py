# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nodes = [(root, str(root.val))]
        total = 0

        while nodes:
            node, num = nodes.pop()
            if node.left:
                nodes.append((node.left, num + str(node.left.val)))
            if node.right:
                nodes.append((node.right, num + str(node.right.val)))
            if not node.left and not node.right:
                total += int(num)

        print(total)
        return total


if __name__ == "__main__":
    # Input: root = [1,2,3]
    # Output: 25
    # Explanation:
    # The root-to-leaf path 1->2 represents the number 12.
    # The root-to-leaf path 1->3 represents the number 13.
    # Therefore, sum = 12 + 13 = 25.
    output = 25
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    assert Solution().sumNumbers(root) == output
