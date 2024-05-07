#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
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
    Use stack to process from back to front
    '''
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next
        addOne = False
        while stack:
            temp = stack.pop()
            temp.val *= 2
            if addOne: 
                temp.val += 1
                addOne = False
            if temp.val >= 10:
                addOne = True
                if not stack:
                    stack.append(ListNode(0, temp))
            temp.val %= 10
        return temp

        
# @lc code=end

