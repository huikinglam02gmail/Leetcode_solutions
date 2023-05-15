#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
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
    Find length of the whole list first
    Then locate nodes k and n - k
    '''
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        i, j = None, None
        temp = head
        count =  0
        while temp:
            count += 1
            if count == k:
                i = temp
            if count == n + 1 - k:
                j = temp
            temp = temp.next
        temp = i.val
        i.val = j.val
        j.val = temp
        return head
# @lc code=end

