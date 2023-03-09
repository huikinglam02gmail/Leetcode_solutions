#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        fast = head
        slow = head        
        while fast.next and slow.next and fast.next.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
            if fast == slow:
                slow = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
# @lc code=end

