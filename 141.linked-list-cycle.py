#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class Solution:
    '''
    turtoise and hare algorithm    
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        if head is None:
            return False
        while fast.next and slow.next and fast.next.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
            if fast == slow:
                return True
        return False
# @lc code=end

