#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
from collections import deque
from typing import List

class UnionFindSet:
    def __init__(self, n=0):
        self.parents = [i for i in range(n)]
        self.count = n
        self.areas = [0] * n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            pMax, pMin = max(pu,pv), min(pu,pv)
            self.parents[pMax] = pMin
            self.count -= 1
    
    def CalAreas(self):
        for i in range(len(self.parents)): self.areas[self.find(i)] += 1

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        UF = UnionFindSet(len(grid) * len(grid))
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    neigs = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
                    for x, y in neigs:
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            UF.union(n * i + j, n * x + y)
        
        UF.CalAreas()
        result = max(UF.areas)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    neigs = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
                    for x, y in neigs:
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and UF.find(n * x + y) not in seen: seen.add(UF.find(n * x + y))
                    result = max(result, 1 + sum([UF.areas[ind] for ind in seen]))
        return result


# @lc code=end

