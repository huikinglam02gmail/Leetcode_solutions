#
# @lc app=leetcode id=3493 lang=python3
#
# [3493] Properties Graph
#

# @lc code=start
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
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        UF = UnionFindSet(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if len(set(properties[i]) & set(properties[j])) >= k: UF.union(i, j)
        return UF.count
# @lc code=end

