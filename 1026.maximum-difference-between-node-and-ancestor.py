#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # We are looking for absolute differences between a node's val and all of its descendents. The parents will be taken care of by a recursive function (dfs)
    # To simplify the process and get the absolute difference between a node and all its offspring, for example between a and {b1, b2, b3...}
    # We can sort bns. Assume smallest is b1 and largest is bn
    # When we calculate the maximum difference, the answer is max(abs(a-b1), abs(a-bn))
    # As for the recursive nature, we return and max and min of {a, b1,..., bn} for a's parent
    
    def dfs(self, root):
        result = [root.val, root.val]
        if root.left:
            left_min, left_max = self.dfs(root.left)
            self.ans = max(self.ans, abs(root.val - left_min), abs(root.val - left_max))
            result = min(result[0], left_min), max(result[1], left_max)
        if root.right:
            right_min, right_max = self.dfs(root.right)
            self.ans = max(self.ans, abs(root.val - right_min), abs(root.val - right_max))
            result = min(result[0], right_min), max(result[1], right_max)
        return result
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        result = self.dfs(root)
        return self.ans
# @lc code=end

