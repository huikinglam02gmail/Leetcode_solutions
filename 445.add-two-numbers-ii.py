#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        head1, head2 = ListNode(0, l1), ListNode(0, l2)
        temp1, temp2 = head1, head2
        while temp1.next != None:
            stack1.append(temp1)
            temp1 = temp1.next
        while temp2.next != None:
            stack2.append(temp2)
            temp2 = temp2.next
        if len(stack1) < len(stack2):
            stack1, stack2 = stack2, stack1
            temp1, temp2 = temp2, temp1
            head1, head2 = head2, head1
        while stack1:
            a, b = divmod(temp1.val + temp2.val, 10)
            stack1[-1].val += a
            temp1.val = b
            temp1 = stack1.pop()
            if stack2:
                temp2 = stack2.pop()
        return head1 if head1.val > 0 else head1.next
 
# @lc code=end

