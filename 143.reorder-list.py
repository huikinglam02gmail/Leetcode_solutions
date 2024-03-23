#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
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
    Use turtle and hare algorithm to find mid point.
    Reverse the latter half
    Merge the two LL
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next: return head
        slow = head
        fast = head
        sPrev = None
        while fast and fast.next:
            sPrev = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            sPrev = sPrev.next
            slow = slow.next
        sPrev.next = None
        sPrev = sPrev.next
        while slow:
            sNext = slow.next
            slow.next = sPrev
            sPrev = slow
            slow = sNext
        temp1 = head
        temp2 = sPrev
        while temp1:
            temp1Next = temp1.next
            temp1.next = temp2
            temp2 = temp1Next
            temp1 = temp1.next
# @lc code=end

