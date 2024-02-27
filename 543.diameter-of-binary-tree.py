#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, node):
        if not node : return 0
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        self.result = max(self.result, left + right)
        return 1 + max(left, right) 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        rootMaxDepth = self.maxDepth(root)
        return self.result
        
# @lc code=end

