#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def generate(self, arr):
        root = None
        if len(arr) > 0:
            left, right = 0, len(arr)-1
            mid = (left + right) // 2
            root = TreeNode(arr[mid])
            root.left = self.generate(arr[:mid])
            root.right = self.generate(arr[mid+1:])
        return root
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        result = []
        temp = head
        while temp:
            result.append(temp.val)
            temp = temp.next
        return self.generate(result)
# @lc code=end

