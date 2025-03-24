#
# @lc app=leetcode id=3067 lang=python3
#
# [3067] Count Pairs of Connectable Servers in a Weighted Tree Network
#

# @lc code=start
from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        self.graph = [set() for i in range(len(edges) + 1)]
        for a, b, w in edges:
            if b not in self.graph[a]: self.graph[a] = {}
            self.graph[a][b] = w
            if a not in self.graph[b]: self.graph[b] = {}
            self.graph[b][a] = w
        

    def dfs(self, node, prev):
        pathSums = []
        for nxt in self.graph[node]:
            if nxt != prev:
                childrenPathSums = self.dfs(nxt, node)
                pathSums.append([])
                pathSums[-1].append([self.graph[node][nxt]])
                for childrenPathSum in childrenPathSums: 
                    pathSums[-1].append(self.graph[node][nxt] + childrenPathSum)
        return pathSums        
# @lc code=end

