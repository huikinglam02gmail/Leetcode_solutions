#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
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
    Two pointer: l stands on a node with 0 and r proceeds forward
    '''
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r, S = head, head.next, 0
        lPrev = ListNode(0, l)
        while r:
            if r.val > 0:
                S += r.val
            else:
                l.val = S
                S = 0
                l.next = r
                lPrev = lPrev.next
                l = l.next
            r = r.next
        lPrev.next = None
        return head

# @lc code=end

