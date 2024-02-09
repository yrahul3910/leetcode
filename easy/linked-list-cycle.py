# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        left = head
        right = head

        while head.next is not None:
            left = left.next

            if right is None or right.next is None:
                return False
            
            right = right.next.next
            if right is not None and left == right:
                return True
        
        return False

