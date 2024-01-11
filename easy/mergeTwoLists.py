# https://leetcode.com/problems/merge-two-sorted-lists/


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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if None in (list1, list2):
            return list1 or list2 or None

        res_head = None
        cur, cur1, cur2 = None, list1, list2

        while cur1 and cur2:
            if not cur:
                if cur1.val <= cur2.val:
                    cur = cur1
                    cur1 = cur1.next
                else:
                    cur = cur2
                    cur2 = cur2.next
                res_head = cur
            else:
                if cur1.val <= cur2.val:
                    new = cur1
                    cur1 = cur1.next
                else:
                    new = cur2
                    cur2 = cur2.next
                cur.next = new
                cur = new

        cur.next = cur1 or cur2 or None

        return res_head


if __name__ == "__main__":
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    res = [1, 1, 2, 3, 4, 4]
    l1_head = create(l1)
    l2_head = create(l2)
    res_head = create(res)
    assert Solution().mergeTwoLists(l1_head, l2_head).equal(res_head)

    l1 = []
    l2 = []
    res = []
    l1_head = create(l1)
    l2_head = create(l2)
    res_head = create(res)
    assert Solution().mergeTwoLists(l1_head, l2_head) is res_head

    l1 = []
    l2 = [0]
    res = [0]
    l1_head = create(l1)
    l2_head = create(l2)
    res_head = create(res)
    assert Solution().mergeTwoLists(l1_head, l2_head).equal(res_head)
