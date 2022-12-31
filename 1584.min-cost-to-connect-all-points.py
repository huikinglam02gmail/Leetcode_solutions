#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
import heapq
from typing import List

class UnionFindSet:
    def __init__(self, n=0):
        self.parents = [i for i in range(n)]
        self.count = n

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

class Solution:
    # This is equivalent to find the minimum spanning tree
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = []
        for i in range(n-1):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                heapq.heappush(heap, [abs(xi - xj) + abs(yi - yj), i, j])
        
        DSU = UnionFindSet(n)
        result = 0
        while DSU.count > 1:
            distance, u, v = heapq.heappop(heap)
            if DSU.find(u) != DSU.find(v):
                DSU.union(u,v)
                result += distance
        return result
# @lc code=end

