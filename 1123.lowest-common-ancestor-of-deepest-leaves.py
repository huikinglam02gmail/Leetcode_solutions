#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
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
    def deep(self, root):
        if not root: return [0, None]
        l, r = self.deep(root.left), self.deep(root.right)
        if l[0] > r[0]: return [l[0] + 1, l[1]]
        elif l[0] < r[0]: return [r[0] + 1, r[1]]
        else: return [l[0] + 1, root]

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.deep(root)[1]
# @lc code=end

