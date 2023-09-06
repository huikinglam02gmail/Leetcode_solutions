#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
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
    First find the length of the linked list
    Then each part should have n//k nodes
    Except the front n%k ones will have 1 more    
    '''
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        n = 0
        while temp:
            n += 1
            temp = temp.next
        result = []
        temp = head
        for j in range(k):
            temp_head = temp
            if j < n % k:
                thres = n // k + 1
            else:
                thres = n // k
            if thres > 0:
                count = 0
                while count < thres:
                    count += 1
                    if count == thres:
                        temp_tail = temp
                    temp = temp.next
                temp_tail.next = None
            result.append(temp_head)
        return result
# @lc code=end

