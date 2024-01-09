#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
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
    dfs by post order traversal and record leaves    
    '''
    def dfs(self, root):
        result = []
        if root.left:
            result += self.dfs(root.left)
        if root.right:
            result += self.dfs(root.right)
        if not root.left and not root.right:
            result += [root.val]
        return result
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafseq1 = self.dfs(root1)
        leafseq2 = self.dfs(root2)
        if len(leafseq1) != len(leafseq2):
            return False
        for v1, v2 in zip(leafseq1, leafseq2):
            if v1 != v2: return False
        return True
# @lc code=end

