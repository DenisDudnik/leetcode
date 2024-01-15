# https://leetcode.com/problems/reverse-linked-list-ii/

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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        new_head = cur
        if not cur.next or left == right:
            return cur

        idx, pre_left_node, left_node, prev_node = 1, None, None, None
        while cur:
            if idx == left - 1:
                pre_left_node = cur
                prev_node = cur
                cur = cur.next
            elif idx == left:
                left_node = cur
                prev_node = cur
                cur = cur.next
            elif idx > left and idx < right:
                next_node = cur.next
                cur.next = prev_node
                prev_node = cur
                cur = next_node
            elif idx == right:
                if pre_left_node:
                    pre_left_node.next = cur
                else:
                    new_head = cur
                left_node.next = cur.next
                cur.next = prev_node
                break
            else:
                cur = cur.next
            idx += 1
        print(new_head)
        return new_head


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    res = [1, 2, 4, 3, 5]
    left = 3
    right = 4
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().reverseBetween(l1_head, left, right).equal(res_head)

    l1 = [1, 2, 3, 4, 5]
    res = [1, 4, 3, 2, 5]
    left = 2
    right = 4
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().reverseBetween(l1_head, left, right).equal(res_head)

    l1 = [5]
    res = [5]
    left = 1
    right = 1
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().reverseBetween(l1_head, left, right).equal(res_head)

    l1 = [3, 5]
    res = [3, 5]
    left = 1
    right = 1
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().reverseBetween(l1_head, left, right).equal(res_head)

    l1 = [3, 5]
    res = [5, 3]
    left = 1
    right = 2
    l1_head = create(l1)
    res_head = create(res)
    assert Solution().reverseBetween(l1_head, left, right).equal(res_head)
