# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def add(self, x):
        new = Node(x)
        self.next = new
        return new

    def equal(self, other) -> bool:
        while self and other and self.val == other.val and id(self) != id(other):
            self = self.next
            other = other.next
        if not self and not other:
            return True
        return False

    def __str__(head):
        cur = head
        lst = []
        visited_nodes = []
        while cur and cur not in visited_nodes:
            visited_nodes.append(cur)
            lst.append(str(cur.val))
            cur = cur.next

        return " -> ".join(lst)


def create(head, pos=-1):
    head_0 = None
    link_here = None
    nodes = []
    for i, h in enumerate(head):
        if not head_0:
            head_0 = Node(h[0])
            cur = head_0
        else:
            cur = cur.add(h[0])
        nodes.append(cur)
        if i == pos:
            link_here = cur
    if head_0:
        cur.next = link_here
    for i, h in enumerate(head):
        nodes[i].random = nodes[h[1]] if h[1] else None
    return head_0


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        cur = head
        while cur:
            new = Node(cur.val, cur.next, cur.random)
            cur.next = new
            cur = new.next

        cur = head.next
        while cur:
            if cur.random:
                cur.random = cur.random.next
            if cur.next:
                cur.next = cur.next.next
            cur = cur.next

        return head.next


if __name__ == "__main__":
    head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    res = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    l1_head = create(head)
    res_head = create(res)
    assert Solution().copyRandomList(l1_head).equal(res_head)
