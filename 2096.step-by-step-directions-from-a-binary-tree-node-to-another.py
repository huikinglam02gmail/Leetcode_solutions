#
# @lc app=leetcode id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
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
    Build the graph first, DFS from root to startValue to get how many layers need 
    '''
    def countNodes(self, node):
        result = 1
        if node.left: result += self.countNodes(node.left)
        if node.right: result += self.countNodes(node.right)
        return result
    
    def buildGraph(self, node):
        if node.left:
            self.graph[node.val - 1]["L"] = node.left.val - 1
            self.graph[node.left.val - 1]["U"] = node.val - 1
            self.buildGraph(node.left)
        if node.right:
            self.graph[node.val - 1]["R"] = node.right.val - 1
            self.graph[node.right.val - 1]["U"] = node.val - 1
            self.buildGraph(node.right)

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        n = self.countNodes(root)
        self.graph = [{} for i in range(n)]
        self.buildGraph(root)

        dq = deque()
        visited = [False] * n
        dq.append([startValue - 1, ""])
        visited[startValue - 1] = True
        while dq:
            nodeVal, pathString = dq.popleft()
            if nodeVal == destValue - 1: return pathString
            for nxt in self.graph[nodeVal]:
                if not visited[self.graph[nodeVal][nxt]]:
                    visited[self.graph[nodeVal][nxt]] = True
                    dq.append([self.graph[nodeVal][nxt], pathString + nxt])
        return "Not found"
# @lc code=end

