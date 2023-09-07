#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    '''
    Use stack
    '''
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        dummy = ListNode(-1, head)
        prev = dummy
        temp = head
        stack = []
        while temp:
            if left <= i <= right:
                stack.append(temp)
            if i == left:
                start = prev
            prev = prev.next
            temp = temp.next
            i += 1
        if stack:
            last = stack[-1].next
        else:
            last = None
        while stack:
            start.next = stack.pop()
            start = start.next
        start.next = last
        return dummy.next
# @lc code=end

