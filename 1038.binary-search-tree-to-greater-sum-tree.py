#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    opposite of in-order traversal, right, mid, left
    save the cumulative sum    
    '''
    def dfs(self, root):
        if root.right: self.dfs(root.right)
        self.cusum += root.val
        root.val = self.cusum
        if root.left: self.dfs(root.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root: return root
        else:
            self.cusum = 0
            self.dfs(root)
            return root
        
# @lc code=end

