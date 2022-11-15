#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        count = 0
        while root.left:
            count += 1
            root = root.left
        return count
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return 1
        if not root.right:
            return 2
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        counter = 1
        if left_height == right_height:
            for i in range(left_height+1):
                counter += pow(2,i)
            return counter + self.countNodes(root.right)
        else:
            for i in range(right_height+1):
                counter += pow(2,i)
            return counter + self.countNodes(root.left)
# @lc code=end

