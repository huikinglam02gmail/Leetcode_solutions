#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
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
    Recursive function
    As number of nodes might be 0, The function will including the case in which root1 and root2 might be null    
    '''
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return True
        if not root1 and root2: return False
        if root1 and not root2: return False
        if root1.val != root2.val: return False
        normal = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        flipped = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        return normal or flipped
# @lc code=end

