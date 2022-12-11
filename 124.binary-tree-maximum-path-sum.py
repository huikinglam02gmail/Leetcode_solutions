#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
    # maximum sum path might be:
    # 1. only at the current node
    # 2. confine to current node and the left subtree
    # 3. confine to current node and the right subtree
    # 4. confine to the left subtree
    # 5. confine to the right subtree
    # 6. Pass from left to right subtree, through the current node

    def traversal(self, root):
        if not root:
            return -float('inf')
        else:
            left = self.traversal(root.left)
            right = self.traversal(root.right)
            passthrough_max = max(root.val, root.val + left, root.val + right)
            nonpassthrough_max = max(left, right, left + right + root.val)
            self.result = max(self.result, nonpassthrough_max)
            return passthrough_max
            
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = -float('inf')
        root_val = self.traversal(root)
        return max(root_val, self.result)
# @lc code=end

