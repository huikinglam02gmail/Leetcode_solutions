#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
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
    '''
    BFS from root to leaf, keep summing
    '''
           
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        dq = deque()
        dq.append([root, ""])
        while dq:
            node, s = dq.popleft()
            if node.left:
                dq.append([node.left, s + str(node.val)])
            if node.right:
                dq.append([node.right, s + str(node.val)])
            if not node.left and not node.right:
                result += int(s + str(node.val))
        return result
# @lc code=end

