#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        step = 0
        while step < a - 1:
            temp = temp.next
            step += 1
        aNode = temp
        while step <= b:
            temp = temp.next
            step += 1
        bNode = temp
        aNode.next = list2
        temp = aNode
        while temp.next != None:
            temp = temp.next
        temp.next = bNode
        return list1
        
# @lc code=end

