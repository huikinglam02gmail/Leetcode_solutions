#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
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
    BFS from the root
    each time we just add the root val to the left of the string
    When we arrive at a leaf, not node.left and not node.right, we put our result into the bank    
    '''
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = ""
        dq = deque()
        dq.append([root, chr(root.val + ord('a'))])
        while dq:
            node, string = dq.popleft()
            if not node.left and not node.right:
                if len(result) == 0: result = string
                else: result = min(result, string)
            if node.left: dq.append([node.left, chr(node.left.val + ord('a')) + string])
            if node.right: dq.append([node.right, chr(node.right.val + ord('a')) + string])
        return result
# @lc code=end

