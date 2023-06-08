# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        current = head
        while current:
            right = current.next
            current.next = left
            left = current
            current = right
        return left

if __name__ == "__main__":
    input_values = range(4)        # Input
    head = ListNode(input_values[0])
    current = head
    for val in input_values[1:]:
        prev = current
        current = ListNode(val)
        prev.next = current
    
    print(head)
    print(Solution().reverseList(head))