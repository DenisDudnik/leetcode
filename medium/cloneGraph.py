# https://leetcode.com/problems/clone-graph/

from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node
        if not node.neighbors:
            return Node(node.val)

        nodes, new_nodes = {}, {}
        stack = [node]

        while stack:
            s = stack.pop()
            if s.val not in nodes:
                nodes[s.val] = s
                new_nodes[s.val] = Node(s.val, [])
                for neighbor in s.neighbors:
                    stack.append(neighbor)

        for k in new_nodes:
            for neighbor in nodes[k].neighbors:
                new_nodes[k].neighbors.append(new_nodes[neighbor.val])

        return new_nodes[1]


if __name__ == "__main__":
    # Input: Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_2, node_4]
    node_4.neighbors = [node_1, node_3]

    Solution().cloneGraph(node_1)
