#
# @lc app=leetcode id=2872 lang=python3
#
# [2872] Maximum Number of K-Divisible Components
#

# @lc code=start
from typing import List


class Solution:
    def dfs(self, node, prev):
        result = self.values[node]
        for nxt in self.graph[node]:
            if nxt != prev:
                current = self.dfs(nxt, node)
                if current % self.k == 0: self.result += 1
                else: result += current
        return result
        
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        self.graph =  [set() for i in range(n)]
        for a, b in edges:
            self.graph[a].add(b)
            self.graph[b].add(a)
        
        self.k = k
        self.result = 0
        self.values = values
        rootSum = self.dfs(0, -1)
        return self.result + 1

# @lc code=end

