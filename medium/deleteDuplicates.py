# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head

        # new_head = None
        # left_node = head
        # last_added_node = None
        # cur = head.next
        # duplicated = False

        # while cur:
        #     if cur.val == left_node.val:
        #         duplicated = True
        #         cur = cur.next
        #         continue
        #     if not duplicated:
        #         if last_added_node:
        #             last_added_node.next = left_node
        #         last_added_node = left_node
        #         if not new_head:
        #             new_head = last_added_node
        #     left_node = cur
        #     duplicated = False
        #     cur = cur.next

        # if left_node and not duplicated:
        #     if last_added_node:
        #         last_added_node.next = left_node
        #         last_added_node = last_added_node.next
        #     else:
        #         new_head = left_node
        #         new_head.next = None

        # if last_added_node:
        #     last_added_node.next = None

        # print(new_head)
        # return new_head

        current = head
        dummy = ListNode(0, current)
        previous = dummy

        while current:
            while current.next and current.val == current.next.val:
                current = current.next

            if previous.next == current:
                previous = previous.next
            else:
                previous.next = current.next
            current = current.next

        print(dummy.next)
        return dummy.next


if __name__ == "__main__":
    l1 = [1, 2, 3, 3, 4, 4, 5]
    res = [1, 2, 5]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().deleteDuplicates(l1_head).equal(res_head)

    l1 = [1, 1, 1, 2, 3]
    res = [2, 3]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().deleteDuplicates(l1_head).equal(res_head)

    l1 = [1, 1, 2]
    res = [2]
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().deleteDuplicates(l1_head).equal(res_head)
