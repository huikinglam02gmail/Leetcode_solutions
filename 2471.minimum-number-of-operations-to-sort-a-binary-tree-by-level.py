#
# @lc app=leetcode id=2471 lang=python3
#
# [2471] Minimum Number of Operations to Sort a Binary Tree by Level
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
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        result = 0
        dq.append(root)
        while dq:
            arr = []
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
                arr.append(node.val)
            result += self.minSwaps(arr)
        return result
                
     
    def minSwaps(self, arr):
        n = len(arr)
        arrpos = [*enumerate(arr)]
        arrpos.sort(key = lambda it : it[1])
        vis = [False for i in range(n)]
        ans = 0
        for i in range(n):
            if vis[i] or arrpos[i][0] == i: continue
            cycle_size = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = arrpos[j][0]
                cycle_size += 1

            if cycle_size > 0: ans += (cycle_size - 1)
        return ans
# @lc code=end

