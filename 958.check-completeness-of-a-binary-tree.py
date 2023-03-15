#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
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
    Simple. Just breadth-first search from root. When we insert into root, we insert the node count as well. For example, in the first node, we have i = 1. Then it's left child has count of 2*i and right child has count of 2*i+1    
    '''

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        dq, total = deque(), 0
        dq.append([root, 1])
        while dq:
            for i in range(len(dq)):
                node, count = dq.popleft()
                total += 1
                if count != total:
                    return False
                if node.left:
                    dq.append([node.left, 2*count])
                if node.right:
                    dq.append([node.right, 2*count + 1])
        return True
# @lc code=end

