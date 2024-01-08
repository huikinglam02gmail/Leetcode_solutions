#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        elif low < root.val and high < root.val:
            return self.rangeSumBST(root.left, low, high)
        elif low > root.val and high > root.val:
            return self.rangeSumBST(root.right, low, high)
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
# @lc code=end

