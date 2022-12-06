#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            odd = None
            even = None
            count = 0
            temp = head
            while temp:
                if not odd:
                    if count == 0:
                        odd = temp
                        temp_odd = temp
                else:
                    if count % 2 == 0:
                        temp_odd.next = temp
                        temp_odd = temp_odd.next
                if not even:
                    if count == 1:
                        even = temp
                        temp_even = temp
                else:
                    if count % 2 == 1:
                        temp_even.next = temp
                        temp_even = temp_even.next
                temp = temp.next
                count += 1
            temp_even.next = None
            temp_odd.next = even
            return odd
# @lc code=end

