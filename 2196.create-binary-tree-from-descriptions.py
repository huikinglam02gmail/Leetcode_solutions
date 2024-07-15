#
# @lc app=leetcode id=2196 lang=python3
#
# [2196] Create Binary Tree From Descriptions
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    '''
    Find the root first: the node without a parent
    Then construct the tree
    '''

    def constructTree(self, rootVal):
        if rootVal == 0: return None
        root = TreeNode(rootVal, None, None)
        if rootVal in self.children:
            root.left = self.constructTree(self.children[rootVal][0])
            root.right = self.constructTree(self.children[rootVal][1]) 
        return root

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        self.children = {}
        parents = {}
        nodesSeen = set()
        for p, c, isLeft in descriptions:
            parents[c] = p
            if p not in self.children: self.children[p] = [0, 0]
            self.children[p][1 - isLeft] = c
            nodesSeen.add(p)
            nodesSeen.add(c)
        
        rootVal = 0
        for node in nodesSeen:
            if node not in parents:
                rootVal = node
                break
        
        return self.constructTree(rootVal)
        
        
# @lc code=end

