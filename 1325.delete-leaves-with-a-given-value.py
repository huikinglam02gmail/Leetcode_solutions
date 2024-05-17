#
# @lc app=leetcode id=1325 lang=python3
#
# [1325] Delete Leaves With a Given Value
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
    Clearly we must use DFS to achieve that    
    '''
    def dfs(self, node, target):
        if not node:
            return None
        node.left = self.dfs(node.left, target)
        node.right = self.dfs(node.right, target)        
        if not node.left and not node.right and node.val == target:
            return None
        else:
            return node
        
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.dfs(root, target)
# @lc code=end

