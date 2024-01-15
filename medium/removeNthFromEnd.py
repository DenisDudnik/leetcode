#


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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return slow.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        print(head)
        return head


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    res = [1, 2, 3, 5]
    n = 2
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().removeNthFromEnd(l1_head, n).equal(res_head)

    l1 = [1]
    res = []
    n = 1
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().removeNthFromEnd(l1_head, n) is None

    l1 = [1, 2]
    res = [1]
    n = 1
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().removeNthFromEnd(l1_head, n).equal(res_head)

    l1 = [1, 2, 3]
    res = [2, 3]
    n = 3
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().removeNthFromEnd(l1_head, n).equal(res_head)
