#
# @lc app=leetcode id=2476 lang=python3
#
# [2476] Closest Nodes Queries in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect_left, bisect_right
from typing import List, Optional


class Solution:
    '''
    Traversing the tree is pain in the butt. Get the whole tree out and binary search
    '''
    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.left)
            self.orderedList.append(root.val)
            self.inOrderTraversal(root.right)

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        self.orderedList = []
        self.inOrderTraversal(root)
        result = []
        for q in queries:
            indLeft = bisect_right(self.orderedList, q) - 1
            indRight = bisect_left(self.orderedList, q)
            if 0 <= indLeft < len(self.orderedList): left = self.orderedList[indLeft]
            else: left = -1
            if 0 <= indRight < len(self.orderedList): right = self.orderedList[indRight]
            else: right = -1            
            result.append([left, right])
        return result
    # @lc code=end

