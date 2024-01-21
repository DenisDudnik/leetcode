# https://leetcode.com/problems/reverse-nodes-in-k-group/

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head

        def reverse_k(left: ListNode, k) -> tuple[ListNode, ListNode]:
            cur, i = left, 1

            while i <= k and cur:
                if i == 1:
                    first = cur
                    next_node = cur.next
                elif i > 1 and i < k:
                    next_node = cur.next
                    cur.next = first
                    first = cur
                else:
                    next_node = cur.next
                    cur.next = first
                    left.next = next_node
                    return cur, next_node
                cur = next_node
                i += 1

        left, right, dummy, i = head, head, ListNode(), 1
        pre = dummy

        while True:
            while right and i < k:
                right = right.next
                i += 1
            i = 1

            if right:
                pre.next, next_node = reverse_k(left, k)
                pre = left
                left = next_node
                right = next_node
            else:
                dummy.next = dummy.next or left
                return dummy.next


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    k = 2
    res = [2, 1, 4, 3, 5]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().reverseKGroup(l1_head, k).equal(res_head)

    l1 = [1, 2, 3, 4, 5]
    k = 3
    res = [3, 2, 1, 4, 5]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().reverseKGroup(l1_head, k).equal(res_head)

    l1 = [1, 2, 3, 4, 5, 6]
    k = 3
    res = [3, 2, 1, 6, 5, 4]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().reverseKGroup(l1_head, k).equal(res_head)
