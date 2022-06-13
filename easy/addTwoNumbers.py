# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
from itertools import zip_longest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = [0]
        for el in zip_longest(l1, l2, fillvalue=0):
            x = res[-1] + sum(el)
            res[-1] = x % 10
            res.append(x // 10)
        if res[-1] == 0:
            res.pop()
        return res


if __name__ == "__main__":
    assert Solution().addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4]) == [7, 0, 8]
    assert Solution().addTwoNumbers(l1=[0], l2=[0]) == [0]
    assert Solution().addTwoNumbers(l1=[9, 9, 9, 9, 9, 9, 9], l2=[9, 9, 9, 9]) == [
        8,
        9,
        9,
        9,
        0,
        0,
        0,
        1,
    ]
