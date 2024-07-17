#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
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
    '''
    This is conceptually similar to Leetcode 1080. Insufficient Nodes in Root to Leaf Paths
    We dfs from root to leaf to search for values in to_delete
    The return value is whether this node is to be deleted
    Because in binary tree, a node does not tell who its parent is
    So if we see one of the child is to be deleted, we severe the bond
    On the other hand, if we find the node is to be deleted, ww can directly put the okay children into self.result    
    '''

    def istokeep(self, root):
        keep_root = root.val not in self.delete
        if root.left:
            keep_left_root = self.istokeep(root.left)
            if not keep_root and keep_left_root: self.result.append(root.left)
            if keep_root and not keep_left_root: root.left = None
        if root.right:
            keep_right_root = self.istokeep(root.right)
            if not keep_root and keep_right_root: self.result.append(root.right)
            if keep_root and not keep_right_root: root.right = None
        return keep_root
    
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.delete, self.result = set(to_delete), []
        if self.istokeep(root): self.result.append(root)
        return self.result
# @lc code=end

