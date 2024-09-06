# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# @lc app=leetcode id=3217 lang=python3
#
# [3217] Delete Nodes From Linked List Present in Array
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class Solution:
    '''
    store nums in hashset
    use a dummy ListNode to point to head, then use two pointers and 
    '''
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        back = dummy
        numSet = set(nums)
        while back and back.next:
            front = back.next
            while front and front.val in numSet: front = front.next
            back.next = front
            back = back.next
        return dummy.next
        
        
# @lc code=end

