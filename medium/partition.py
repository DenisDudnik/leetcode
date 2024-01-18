# https://leetcode.com/problems/partition-list/

"""
The rules are:

Any number that is less than x has to be before x, and maintain the relative order with thoese that are less than x
but already before x.
e.g. [3,4,1,2], target = 4 -> [3,1,2,4], so the order of [3,1,2] is maintained.
Any number that is greater than x but already before x will still be before x, but all of them come after those that are
less than x and at the same time maintain their relative order.
e.g. [3,6,5,4,1,2] target = 4 -> [3,1,2,6,5,4]
Any number that is greater than x and after x will only need to maintain their relative order
e.g. [3,6,5,4,8,1,7,2] target = 4 -> [3,1,2,6,5,4,8,7]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, x):
        new = ListNode(x)
        self.next = new
        return new

    def equal(self, other) -> bool:
        while self and other and self.val == other.val:
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
        if cur in visited_nodes:
            lst.append("Cicle!!!")

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
    if head_0:
        cur.next = link_here
    return head_0


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left_head, center_head, right_head, cur, found_x = ListNode(), ListNode(), ListNode(), head, False
        left, center, right = left_head, center_head, right_head
        while cur:
            if cur.val == x:
                found_x = True
            if cur.val < x:
                left.next = cur
                left = left.next
            elif not found_x:
                center.next = cur
                center = center.next
            else:
                right.next = cur
                right = right.next
            cur = cur.next
        left.next = center_head.next or right_head.next
        center.next = right_head.next
        right.next = None

        print(left_head.next)
        return left_head.next


if __name__ == "__main__":
    l1 = [1, 4, 3, 2, 5, 2]
    x = 3
    res = [1, 2, 2, 4, 3, 5]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().partition(l1_head, x).equal(res_head)

    l1 = [2, 1]
    x = 2
    res = [1, 2]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().partition(l1_head, x).equal(res_head)
