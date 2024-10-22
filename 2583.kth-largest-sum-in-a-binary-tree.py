#
# @lc app=leetcode id=2583 lang=python3
#
# [2583] Kth Largest Sum in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        dq = deque()
        dq.append(root)
        step = 0
        levelSums = []
        while dq:
            step += 1
            current = 0
            for i in range(len(dq)):
                node = dq.popleft()
                current += node.val
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            levelSums.append(current)
        return -1 if len(levelSums) < k else sorted(levelSums, reverse=True)[k - 1]
# @lc code=end

