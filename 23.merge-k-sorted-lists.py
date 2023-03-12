#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
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
import heapq
from typing import List, Optional


class Solution:
    # Push all the front nodes to a min heap
    # Then keep moving forward and popping
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, ll in enumerate(lists):
            if ll:
                heapq.heappush(heap, [ll.val,i, ll])
        head, temp = None, None
        while heap:
            v, i, node = heapq.heappop(heap)
            if not head:
                head = node
                temp = head
            else:
                temp.next = node
                temp = temp.next
            if node.next:
                heapq.heappush(heap, [node.next.val, i, node.next])
        if temp:
            temp.next = None
        return head
# @lc code=end

