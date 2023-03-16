#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = None
        if postorder:
            root = TreeNode(postorder[-1])
            left = inorder.index(postorder[-1])
            right =  left + 1
            root.left = self.buildTree(inorder[:left], postorder[:left])
            root.right = self.buildTree(inorder[right:], postorder[left:-1])
        return root        
# @lc code=end

