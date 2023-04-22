#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    '''
    recursive function
    matching nodes: left vs right and right vs left or both empty    
    '''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror_comparison(root, root)
    
    def mirror_comparison(self, node1: Optional[TreeNode], node2: Optional[TreeNode])-> bool:
        if not node1:
            return not node2
        elif not node2:
            return False
        elif node1.val != node2.val:
            return False
        else:
            return self.mirror_comparison(node1.left, node2.right) and self.mirror_comparison(node1.right, node2.left)

# @lc code=end

