#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:
    '''
    BFS and keep …rack of maximum sum seen so far    
    '''
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq, level, max_level, max_so_far = deque(), 1, -1, -float('inf')
        dq.append(root)
        while dq:
            total = 0
            for i in range(len(dq)):
                node = dq.popleft()
                total += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if total > max_so_far:
                max_level= level
                max_so_far = total
            level += 1
        return max_level
            
                
# @lc code=end

