#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List, Optional


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.order_list = []
        self.traversal(root)
        return self.order_list
    
    def traversal(self, root: Optional[TreeNode]):
        if root:
            for child in root.children: self.traversal(child)
            self.order_list.append(root.val)
         
# @lc code=end

