# https://leetcode.com/problems/add-two-numbers/

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2, cur_res = l1, l2, None
        plus_one = 0
        res_head = None

        while cur1 or cur2:
            x = cur1.val if cur1 else 0
            y = cur2.val if cur2 else 0
            z = x + y + plus_one
            plus_one = z // 10
            z %= 10
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            if not res_head:
                res_head = ListNode(z)
                cur_res = res_head
            else:
                new = ListNode(z)
                cur_res.next = new
                cur_res = cur_res.next

        if plus_one:
            new = ListNode(plus_one)
            cur_res.next = new
            cur_res = cur_res.next

        return res_head


if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    res = [7, 0, 8]
    l1_head = create(l1)
    l2_head = create(l2)
    res_head = create(res)
    assert Solution().addTwoNumbers(l1_head, l2_head).equal(res_head)

    l1 = [0]
    l2 = [0]
    res = [0]
    l1_head = create(l1)
    l2_head = create(l2)
    res_head = create(res)
    assert Solution().addTwoNumbers(l1_head, l2_head).equal(res_head)

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    res = [8, 9, 9, 9, 0, 0, 0, 1]
    l1_head = create(l1)
    l2_head = create(l2)
    res_head = create(res)
    assert Solution().addTwoNumbers(l1_head, l2_head).equal(res_head)
