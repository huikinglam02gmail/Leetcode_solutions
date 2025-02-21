#
# @lc app=leetcode id=1261 lang=python3
#
# [1261] Find Elements in a Contaminated Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class FindElements:
    '''
    We first recover the tree and record all tree value in a set
    In the find function, we will search for the target in the set
    '''
    
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen
        
    def dfs(self, node, value):
        node.val = value
        self.seen.add(value)
        if node.left: self.dfs(node.left, 2*value + 1)
        if node.right: self.dfs(node.right, 2*value+2)
        

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end

