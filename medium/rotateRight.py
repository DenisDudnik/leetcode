# https://leetcode.com/problems/rotate-list/

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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or not head or not head.next:
            return head

        left, right, real_shift, length = head, head, None, None
        for i in range(k):
            if right.next:
                right = right.next
            else:
                right = head
                length = i + 1
                real_shift = k % length
            if length and i - length + 1 == real_shift:
                break

        if right == head:
            return head

        while right.next:
            left = left.next
            right = right.next

        new_head = left.next
        right.next = head
        left.next = None

        print(new_head)
        return new_head


if __name__ == "__main__":
    # l1 = [1, 2, 3, 4, 5]
    # k = 2
    # res = [4, 5, 1, 2, 3]
    # l1_head = create(l1)
    # res_head = create(res)
    # assert Solution().rotateRight(l1_head, k).equal(res_head)

    l1 = [0, 1, 2]
    k = 4
    res = [2, 0, 1]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().rotateRight(l1_head, k).equal(res_head)

    l1 = [1, 2]
    k = 0
    res = [1, 2]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().rotateRight(l1_head, k).equal(res_head)

    l1 = [1, 2]
    k = 2
    res = [1, 2]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().rotateRight(l1_head, k).equal(res_head)

    l1 = [1, 2]
    k = 2000000000
    res = [1, 2]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().rotateRight(l1_head, k).equal(res_head)

    l1 = []
    k = 0
    res = []
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().rotateRight(l1_head, k) is None
