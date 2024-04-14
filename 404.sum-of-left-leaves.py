#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        dq, result = deque(), 0
        dq.append(root)
        while dq:
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
                if not node.left.left and not node.left.right:
                    result += node.left.val
            if node.right:
                dq.append(node.right)
        return result
# @lc code=end

