#
# @lc app=leetcode id=2385 lang=python3
#
# [2385] Amount of Time for Binary Tree to Be Infected
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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph, dq = {}, deque()
        dq.append(root)
        if root.val not in graph: graph[root.val] = set()        
        while dq:
            node = dq.popleft()
            if node.left:
                graph[node.val].add(node.left.val)
                if node.left.val not in graph: graph[node.left.val] = set()
                graph[node.left.val].add(node.val)
                dq.append(node.left)
            if node.right:
                graph[node.val].add(node.right.val)
                if node.right.val not in graph: graph[node.right.val] = set()
                graph[node.right.val].add(node.val)
                dq.append(node.right)
        
        result, visited = -1, set()
        dq.append(start)
        visited.add(start)
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                for nxt in graph[node]:
                    if nxt not in visited:
                        visited.add(nxt)
                        dq.append(nxt)
            result += 1
        return result
# @lc code=end

