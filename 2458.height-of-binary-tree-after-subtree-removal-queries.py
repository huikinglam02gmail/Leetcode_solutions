#
# @lc app=leetcode id=2458 lang=python3
#
# [2458] Height of Binary Tree After Subtree Removal Queries
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional


class Solution:
    '''
    First BFS the tree
    Get all the levels of each node (Distance from the root)
    Generate node: level map
    Then DFS the tree to get the maximum depth at each node
    node: (level, maxdepth)
    At the same time, generate the inverse map: level: list of maxdepths
    sort the list
    For each query, find the level of the query node.
    If the node to be removed is the only one in the list of depths, we return level - 1
    else if the node to be removed is the largest one in the list of depths, we ask if it has a same-level neighbour node with same depth. If yes, just return maxDepth of the root
    else, we return level + next largest max depth at the same level
    finally if the node of interest does not have the largest maxdepth, then just return maxDepth of the root    
    '''
    def findmaxDepth(self, node):
        depth = 0
        if node.left:
            depth = max(depth, self.findmaxDepth(node.left) + 1)
        if node.right:
            depth = max(depth, self.findmaxDepth(node.right) + 1)  
        self.hashTable[node.val][1] = depth
        self.levelToDepth[self.hashTable[node.val][0]].append(depth)
        return depth
    
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        dq, level = deque(), 0
        self.hashTable = {}
        dq.append(root)
        self.levelToDepth = []
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                self.hashTable[node.val] = [level, 0]
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1
        self.levelToDepth = [[] for i in range(level)]
        rootDepth = self.findmaxDepth(root)
        for i in range(level):
            self.levelToDepth[i].sort()
        
        result = []
        for query in queries:
            nodeLevel, nodeDepth = self.hashTable[query]
            if len(self.levelToDepth[nodeLevel]) == 1:
                result.append(nodeLevel - 1)
            elif nodeDepth == self.levelToDepth[nodeLevel][-1] and self.levelToDepth[nodeLevel][-2] != nodeDepth:
                result.append(nodeLevel + self.levelToDepth[nodeLevel][-2])
            else:
                result.append(rootDepth)
        return result
# @lc code=end

