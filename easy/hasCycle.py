# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, x):
        new = ListNode(x)
        self.next = new
        return new

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
    for i, h in enumerate(head):
        if not head_0:
            head_0 = ListNode(h)
            cur = head_0
        else:
            cur = cur.add(h)
        if i == pos:
            link_here = cur
    cur.next = link_here
    return head_0


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


if __name__ == "__main__":
    head = [3, 2, 0, -4]
    pos = 1
    head_0 = create(head, pos)
    assert Solution().hasCycle(head_0) == True

    head = [1, 2]
    pos = 0
    head_0 = create(head, pos)
    assert Solution().hasCycle(head_0) == True

    head = [1]
    pos = -1
    head_0 = create(head, pos)
    assert Solution().hasCycle(head_0) == False
