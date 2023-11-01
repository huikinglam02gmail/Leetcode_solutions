#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    '''
    In-order traversal ensures nondecreasing visit
    Save the mode list and mode count, last num and last count
    '''
    def dfs(self, node):
        if node.left:
            self.dfs(node.left)
        if node.val == self.lastNum:
            self.lastCount += 1
        else:
            self.lastNum = node.val
            self.lastCount = 1
        if self.modeCount == self.lastCount:
            self.modeList.append(self.lastNum)
        elif self.modeCount < self.lastCount:
            self.modeList.clear()
            self.modeCount = self.lastCount
            self.modeList.append(self.lastNum)
        if node.right:
            self.dfs(node.right)
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.lastNum = -100001
        self.lastCount = 0
        self.modeCount = 0
        self.modeList = []

        self.dfs(root)
        return self.modeList
# @lc code=end

