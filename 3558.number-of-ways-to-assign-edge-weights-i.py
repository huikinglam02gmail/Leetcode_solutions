#
# @lc app=leetcode id=3558 lang=python3
#
# [3558] Number of Ways to Assign Edge Weights I
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Build the graph and BFS from root to find the max depth
    The number of ways to assign edge weights is sum(maxDepth C (odd)) = 2^(maxDepth - 1)
    '''
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = [set() for _ in range(len(edges) + 1)]
        for u, v in edges:
            graph[u - 1].add(v - 1)
            graph[v - 1].add(u - 1)
        maxDepth = 0
        dq = deque()
        dq.append(0)
        visited = [False] * (len(edges) + 1)
        visited[0] = True
        while dq:
            size = len(dq)
            for _ in range(size):
                node = dq.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        dq.append(neighbor)
            maxDepth += 1
        
        MOD = 1000000007
        return pow(2, maxDepth - 2, MOD)
# @lc code=end

