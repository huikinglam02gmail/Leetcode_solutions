#
# @lc app=leetcode id=3319 lang=python3
#
# [3319] K-th Largest Perfect Subtree Size in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
from typing import Optional


class Solution:
    def dfs(self, node):
        if not node: return 0
        leftCount = self.dfs(node.left)
        rightCount = self.dfs(node.right)
        result = -1
        if leftCount == rightCount and leftCount >= 0 and rightCount >= 0: result = 1 + leftCount + rightCount
        if result > 0: 
            heapq.heappush(self.heap, result)
            while len(self.heap) > self.k: heapq.heappop(self.heap)
        return result

    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []
        self.k = k
        totalCount = self.dfs(root)
        if len(self.heap) < k: return -1
        else: return self.heap[0]
        
# @lc code=end
