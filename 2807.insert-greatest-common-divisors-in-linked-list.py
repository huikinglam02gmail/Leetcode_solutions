#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
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
    For each neighboring node, get a new node with GCD and link them up
    '''
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            mid = ListNode(self.gcd(temp.val, temp.next.val))
            mid.next = temp.next
            temp.next = mid
            temp = temp.next.next
        return head
    
    '''
    Greatest common divisor between a and b
    '''
    def gcd(self, a, b):
        if (a == 0):
            return b
        else:
            return self.gcd(b % a, a)
# @lc code=end

