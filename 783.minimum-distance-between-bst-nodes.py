#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
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
    def dfs(self,root):
        if root.left:
            self.dfs(root.left)
        self.min_diff = min(self.min_diff, root.val -  self.last_node_val)
        self.last_node_val = root.val
        if root.right:
            self.dfs(root.right)
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.last_node_val = -float('inf')
        self.dfs(root)
        return self.min_diff
# @lc code=end

