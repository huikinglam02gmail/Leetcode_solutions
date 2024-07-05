#
# @lc app=leetcode id=2058 lang=python3
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        count = 0
        temp = head
        result = [-1, -1]
        critical = []
        while temp:
            if temp.next and temp.next.next:
                if (temp.val > temp.next.val and temp.next.val < temp.next.next.val) or (temp.val < temp.next.val and temp.next.val > temp.next.next.val):
                    critical.append(count + 1)
            temp = temp.next
            count += 1
        n = len(critical)
        if n > 1: 
            result[1] = critical[-1] - critical[0]
            result[0] = count
            for i in range(n - 1):
                result[0] = min(critical[i + 1] - critical[i], result[0])
        return result
# @lc code=end

