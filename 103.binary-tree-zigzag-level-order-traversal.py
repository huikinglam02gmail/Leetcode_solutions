#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Simple. Just BFS zigzag!
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq, level, result = deque(), 0, []
        if root:
            dq.append(root)
            while dq:
                row = []
                for i in range(len(dq)):
                    node = dq.popleft()
                    row.append(node.val)
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
                if level % 2 == 1:
                    row.reverse()
                result.append(row)
                level += 1
        return result
# @lc code=end

