#
# @lc app=leetcode id=3372 lang=python3
#
# [3372] Maximize the Number of Target Nodes After Connecting Trees I
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    For each node on first tree, BFS in first tree and count # of nodes within k steps
    For each node on second tree, BFS in second tree and count # of nodes within k - 1 steps, find the max
    '''
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        m = len(edges2) + 1
        n = len(edges1) + 1
        graph1 = [set() for i in range(len(edges1) + 1)]
        graph2 = [set() for i in range(len(edges2) + 1)]
        for a, b in edges1:
            graph1[a].add(b)
            graph1[b].add(a)
        for a, b in edges2:
            graph2[a].add(b)
            graph2[b].add(a)

        S = 0
        for i in range(m): S = max(S, self.bfs(graph2, i, k - 1))
        result = []
        for i in range(n): result.append(S + self.bfs(graph1, i, k))
        return result
    
    def bfs(self, graph, startNode, maxStep):
        count = 0
        visited = [False for i in range(len(graph))]
        dq = deque()
        dq.append(startNode)
        visited[startNode] = True
        steps = 0
        while dq and steps <= maxStep:
            for i in range(len(dq)):
                node = dq.popleft()
                count += 1
                for nxt in graph[node]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        dq.append(nxt)
            steps += 1
        return count

# @lc code=end

