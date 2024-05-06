#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevHead = ListNode(100001, head)
        temp = head
        stack = []
        stack.append(prevHead)
        while temp:
            while stack and stack[-1].val < temp.val:
                stack.pop()
            stack[-1].next = temp
            stack.append(temp)
            temp = temp.next
        return prevHead.next

# @lc code=end

