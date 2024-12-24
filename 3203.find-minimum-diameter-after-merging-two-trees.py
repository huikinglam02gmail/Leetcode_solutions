#
# @lc app=leetcode id=3203 lang=python3
#
# [3203] Find Minimum Diameter After Merging Two Trees
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    The answer is among these 3:
    1. Diameter of tree1
    2. Diameter of tree2
    3. link the center of the longest paths in tree1 and tree2
    '''
    def treeDiameter(self, edges):
        graph = [set() for i in range(len(edges) + 1)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        dq = deque()
        visited = [False for i in range(len(edges) + 1)]
        dq.append(0)
        visited[0] = True
        node = -1
        while dq:
            node = dq.popleft()
            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dq.append(nxt)
        diameter = 0
        dq = deque()
        visited = [False for i in range(len(edges) + 1)]
        dq.append(node)
        visited[node] = True
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                for nxt in graph[node]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        dq.append(nxt)
            if dq: diameter += 1
        return diameter

    '''
    ceil division
    '''
    def ceildiv(self, a, b):
        return -(a // -b)

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        d1 = self.treeDiameter(edges1)
        d2 = self.treeDiameter(edges2)
        return max(d1, d2, 1 + self.ceildiv(d1, 2) + self.ceildiv(d2, 2))
# @lc code=end

