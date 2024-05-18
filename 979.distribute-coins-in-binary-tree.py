#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
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
    '''
    We know the final state: node.val = 1 for all node
    Now let's think about the "flux" of coins between parent and its children
    And define that to be the return value of the DFS function
    If positive: coins will be going back to its parent
    If negative: coins will be going from its parent    
    '''  
    def dfs(self, node):
        if not node: return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.result += abs(left) + abs(right)
        return node.val + left + right - 1
    
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.dfs(root)
        return self.result
# @lc code=end

