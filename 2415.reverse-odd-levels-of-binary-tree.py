#
# @lc app=leetcode id=2415 lang=python3
#
# [2415] Reverse Odd Levels of Binary Tree
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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque()
        level = 0
        dq.append(root)
        values = [root.val]
        values_nxt = []
        while dq:
            l = len(dq)
            for i in range(l):
                node = dq.popleft()
                if level % 2 != 0: node.val = values[l - 1 - i]
                if node.left:
                    dq.append(node.left)
                    values_nxt.append(node.left.val)
                if node.right:
                    dq.append(node.right)
                    values_nxt.append(node.right.val)
            values = values_nxt[:]
            values_nxt = []
            level += 1
        return root
            
# @lc code=end

