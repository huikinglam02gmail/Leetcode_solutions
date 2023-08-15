#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # separate the nodes into two groups
    # The first one has nodes with value < x
    # The second one has nodes with value >= x
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        dummy1 = ListNode(-101)
        dummy2 = ListNode(101)
        temp1 = dummy1
        temp2 = dummy2
        while temp:
            if temp.val < x:
                temp1.next = temp
                temp1 = temp1.next
            else:
                temp2.next = temp
                temp2 = temp2.next
            temp = temp.next
        temp2.next = None
        temp1.next = dummy2.next
        return dummy1.next
        
# @lc code=end

