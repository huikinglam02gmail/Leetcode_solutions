#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
    Use tools from Leetcode 655 Print Binary Tree. When doing BFS, the level and position of nodes are recorded. Width of each level is given by recording and subtracting max and min of positions seen so far       
    '''

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append([root,0])
        max_width = 0
        while dq:
            max_pos = -float('Inf')
            min_pos = float('Inf')
            for i in range(len(dq)):
                item = dq.popleft()
                pos = item[1]
                max_pos = max(pos, max_pos)
                min_pos = min(pos, min_pos)
                if item[0].left:
                    dq.append([item[0].left, 2*pos])
                if item[0].right:
                    dq.append([item[0].right, 2*pos + 1])
            max_width = max(max_width, max_pos - min_pos + 1)
        return max_width
# @lc code=end

