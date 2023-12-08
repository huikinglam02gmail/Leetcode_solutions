#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
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
    '''
    DFS is called for here.
    Preorder traversal: root -> left -> right    
    '''

    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""
        if root: 
            result += str(root.val)
            if root.left or root.right:
                result += "(" + self.tree2str(root.left) + ")"
                if root.right:
                    result += "(" + self.tree2str(root.right) + ")"
        return result
# @lc code=end

