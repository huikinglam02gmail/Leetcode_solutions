#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
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
    # We need to calculate subtree sum (STS) for each node
    # for the root, subtree sum = total
    # we are maximizing STS*(total-STS)
    # Just record all STS in a set
    
    def dfs(self, node):
        if not node:
            return 0
        result = node.val + self.dfs(node.left) + self.dfs(node.right)
        self.STS.add(result)
        return result
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.STS = set()
        total, MOD, maxsofar = self.dfs(root), pow(10,9)+7, 0
        for item in self.STS:
            maxsofar = max(maxsofar, item*(total-item))
        return maxsofar % MOD
# @lc code=end

