#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
from typing import List, Optional


class Solution:
    def constructTrees(self, start, end):
        list = []
        if (start > end) :
            list.append(None)
            return list
        for i in range(start, end + 1):
            leftSubtree = self.constructTrees(start, i - 1)
            rightSubtree = self.constructTrees(i + 1, end)

            for j in range(len(leftSubtree)) :
                left = leftSubtree[j]
                for k in range(len(rightSubtree)):
                    right = rightSubtree[k]
                    node = TreeNode(i)   
                    node.left = left    
                    node.right = right   
                    list.append(node)    
        return list

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.constructTrees(1,n)
        
# @lc code=end

