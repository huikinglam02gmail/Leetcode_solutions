#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1 = [set() for i in range(len(edges1) + 1)]
        graph2 = [set() for i in range(len(edges2) + 1)]

        for a,b in edges1:
            graph1[a].add(b)
            graph1[b].add(a)

        for a,b in edges2:
            graph2[a].add(b)
            graph2[b].add(a)
        
        parity1 = self.bfs(graph1)
        parity2 = self.bfs(graph2)

        toAdd = max(len(x) for x in parity2)
        result = []
        for i in range(len(edges1) + 1):
            for j in range(2):
                if i in parity1[j]: result.append(len(parity1[j]) + toAdd)
        return result
    
    def bfs(self, graph):
        parity = [set() for i in range(2)]
        dq = deque()
        steps = 0
        dq.append(0)
        visited = [False for i in range(len(graph))]
        visited[0] = True

        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                parity[steps % 2].add(node)
                for nxt in graph[node]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        dq.append(nxt)
            steps += 1
        
        return parity
        
# @lc code=end

