#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    '''
    Count how many nodes are there first
    In the second traversal, keep two pointers: temp moves one node faster
    Carry out the replacement    
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        counter = 0
        temp = head
        while temp.next:
            counter += 1
            temp = temp.next
        total = counter
        if total < n - 1:
            return None
        elif total == n - 1:
            return head.next
        else:
            counter = 0
            temp = head
            while counter < total - n + 1:
                counter += 1
                temp1 = temp
                temp = temp.next
            temp1.next = temp.next
            return head
            
# @lc code=end

