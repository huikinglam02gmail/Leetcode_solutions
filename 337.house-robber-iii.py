#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
from typing import Optional


class Solution:
        
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dfs(root, robThisNode):
            result = 0
            if root:
                if robThisNode:
                    result += root.val
                    result += dfs(root.left, False)
                    result += dfs(root.right, False)
                else:
                    result += max(dfs(root.left, False), dfs(root.left, True))
                    result += max(dfs(root.right, False), dfs(root.right, True))
            return result

        return max(dfs(root, True), dfs(root, False))
# @lc code=end

