#
# @lc app=leetcode id=2065 lang=python3
#
# [2065] Maximum Path Quality of a Graph
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Try all the paths
    '''
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        self.graph = [{} for i in range(len(values))]
        for u, v, t in edges:
            if v not in self.graph[u]: self.graph[u][v] = 0
            self.graph[u][v] = t
            if u not in self.graph[v]: self.graph[v][u] = 0
            self.graph[v][u] = t
        self.result = 0
        self.maxTime = maxTime
        self.visited = [False for i in range(len(values))]
        self.visited[0] = True
        self.values = values          
        self.dfs(0, values[0], 0)
        return self.result

    def dfs(self, node, value, time):
        if time > self.maxTime: return
        if node == 0: self.result = max(self.result, value)
        for nxt in self.graph[node]:
            if not self.visited[nxt]:
                self.visited[nxt] = True
                self.dfs(nxt, value + self.values[nxt], time + self.graph[node][nxt])
                self.visited[nxt] = False
            else: self.dfs(nxt, value,  time + self.graph[node][nxt])           
# @lc code=end

