#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
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
    conduct BFS when taking note of the depth:    
    '''
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val, root, None)
        dq, dep = deque(), 1
        dq.append(root)
        while dep < depth:
            dep += 1
            for i in range(len(dq)):
                node = dq.popleft()
                if dep == depth:
                    left_node, right_node = node.left, node.right
                    node.left, node.right = TreeNode(val, left_node, None), TreeNode(val, None, right_node)
                else:
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
        return root
# @lc code=end

