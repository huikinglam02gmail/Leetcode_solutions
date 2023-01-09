#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder = []
        self.traversal(root)
        return self.preorder
        
    def traversal(self,root: Optional[TreeNode]):
        if root:
            self.preorder.append(root.val)
            if root.left:
                self.traversal(root.left)
            if root.right:
                self.traversal(root.right)
# @lc code=end

