#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            if node.right:
                dq.append(node.right)
            if node.left:
                dq.append(node.left)
            if not dq:
                return node.val
# @lc code=end

