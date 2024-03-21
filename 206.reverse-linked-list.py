#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
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
    keep three nodes, and flip the next arrow of the middle node
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        temp_prev = None
        while temp:
            temp_next = temp.next
            temp.next = temp_prev
            temp_prev = temp
            temp = temp_next
        head = temp_prev
        return head
# @lc code=end

