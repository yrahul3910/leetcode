# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        head = ListNode()
        tail = head
        while list1 is not None and list2 is not None:
            list3 = ListNode(min(list1.val, list2.val))
            tail.next = list3
            tail = list3

            if list1.val < list2.val:
                list1 = list1.next
            else:
                list2 = list2.next
        
        if list1 is not None:
            tail.next = list1
        if list2 is not None:
            tail.next = list2

        return head.next
        
