#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
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
    Dummy node solves it easily
    '''
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        temp1 = dummy
        while temp1 and temp1.next and temp1.next.next:
            temp2 = temp1.next
            temp3 = temp2.next
            temp1.next = temp3
            temp2.next = temp3.next
            temp3.next = temp2
            temp1 = temp1.next.next
        return dummy.next
        
# @lc code=end

