#
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
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
    palindromes = even appearance in all or all but 1
    We can use BFS from root to obtain all root to leaf paths
    Since the values are only 1-9, we might use bit representation of odd vs even number of occurence seen in the previous path
    '''
    
    def update_state(self, state, num):
        state ^= (1 << (num-1))
        return state
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        dq, result = deque(), 0
        dq.append([root, self.update_state(0, root.val)])
        palindromes = set()
        palindromes.add(0)
        for i in range(9):
            palindromes.add(1 << i)
        while dq:
            node, state = dq.popleft()
            if not node.left and not node.right and state in palindromes:
                result += 1
            if node.left:
                dq.append([node.left, self.update_state(state, node.left.val)])
            if node.right:
                dq.append([node.right, self.update_state(state, node.right.val)])
        return result
# @lc code=end

