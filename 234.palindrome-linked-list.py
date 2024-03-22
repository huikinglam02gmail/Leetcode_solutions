#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
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
    Turtle and hare + reverse linked list:
    If we follow turle and hare algorithm, We know that:
    1. If the number of nodes in the LL is odd, fast will stay on the last node.
    2. If the number of nodes in the LL is even, fast will be null
    For both cases, slow will be at n // 2 th node
    If we reverse the LL while slow progresses, keeping track of sNext and sPrev:
    1. If the number of nodes in the LL is odd s = sNext
    Then we compare values of s and sPrev and progress them.
    '''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        sNext = slow.next
        sPrev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next = sPrev
            sPrev = slow
            slow = sNext
            sNext = slow.next
        if fast:
            slow = slow.next
        while slow:
            if slow.val != sPrev.val: return False
            slow = slow.next
            sPrev = sPrev.next
        return True
        
# @lc code=end

