#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postorder = []
        self.traversal(root)
        return self.postorder
        
    def traversal(self, root: Optional[TreeNode]): 
        if root:
            if root.left:
                self.traversal(root.left)
            if root.right:
                self.traversal(root.right)
            self.postorder.append(root.val)  
# @lc code=end

