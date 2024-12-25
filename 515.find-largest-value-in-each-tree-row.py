#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional


class Solution:
    '''
    Use BFS to find max level by level    
    '''
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        dq = deque()
        if root:
            dq.append(root)
        while dq:
            current_max = - pow(2,31)
            for i in range(len(dq)):
                node = dq.popleft()
                current_max = max(current_max, node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            result.append(current_max)
        return result
# @lc code=end

