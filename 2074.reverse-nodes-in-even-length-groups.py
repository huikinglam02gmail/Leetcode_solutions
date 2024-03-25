#
# @lc app=leetcode id=2074 lang=python3
#
# [2074] Reverse Nodes in Even Length Groups
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
    Keep track of current level length.
    If current level length is even, we record the end of last level. Then move to the next node and start reversing the linked list up to current level length or end
    Then point last.next to the end
    Move the pointer forward by current level length's step
    '''
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentLevelLength = 1
        temp = ListNode(-1, head)
        while temp:
            steps = 0
            temp1 = temp
            while steps <= currentLevelLength and temp1:
                temp1 = temp1.next
                steps += 1
            if steps % 2: self.reverseLLBetweenTwoNodes(temp, temp1)
            steps = 0
            while steps < currentLevelLength and temp:
                temp = temp.next
                steps += 1
            currentLevelLength += 1
        return head
    
    def reverseLLBetweenTwoNodes(self, nodePrev, nodeAfter):
        temp1 = nodePrev.next
        temp1Prev = nodeAfter
        while temp1 != nodeAfter:
            temp1Next = temp1.next
            temp1.next = temp1Prev
            temp1Prev = temp1
            temp1 = temp1Next
        nodePrev.next = temp1Prev
# @lc code=end

