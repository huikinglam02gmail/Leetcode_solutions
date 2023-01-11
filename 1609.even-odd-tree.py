#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:
    # Really simple, just BFS
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        dq = deque()
        dq.append(root)
        while dq:
            if level % 2 == 0:
                prev = 0
            else:
                prev = 1000001
            for i in range(len(dq)):
                node = dq.popleft()
                if (level % 2 == 0 and (node.val <= prev or node.val % 2 == 0)) or (level % 2 == 1 and (node.val >= prev or node.val % 2 == 1)):
                    return False
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                prev = node.val          
            level += 1
        return True
        
# @lc code=end

