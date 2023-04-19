#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
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
class Solution:
    '''
    We can use dfs to return maximum left and right zigzag paths length that originates at the node
    Use a global result variable to keep the maximum length zigzag path seen   
    '''

    def zigzag(self, node):
        res = [0, 0]
        if node.left:
            left_l, left_r = self.zigzag(node.left)
            res[0] = 1 + left_r
        if node.right:
            right_l, right_r = self.zigzag(node.right)
            res[1] = 1 + right_l
        self.result = max(self.result, res[0], res[1])
        return res
        
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        res = self.zigzag(root)
        return self.result
# @lc code=end

