#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
from typing import Optional


class Solution:
    '''
    Use resevoir sampling algorithm
    '''

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        n = 1
        k = 1
        node = self.head
        ans = self.head

        while node.next:
            n += 1
            node = node.next
            if random.random() < k / n:
                ans = ans.next
                k += 1
        return ans.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

