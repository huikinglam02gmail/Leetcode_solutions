#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
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
    keep track of subtree sum and number of nodes in subtree
    '''
    def dfs(self, node):
        if not node:
            return [0, 0]
        else:
            leftSum, leftTotal = self.dfs(node.left)
            rightSum, rightTotal = self.dfs(node.right)
            if node.val == (node.val + leftSum + rightSum) // (1 + leftTotal + rightTotal):
                self.result += 1
            return [node.val + leftSum + rightSum, 1 + leftTotal + rightTotal]

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.dfs(root)
        return self.result
        
# @lc code=end

