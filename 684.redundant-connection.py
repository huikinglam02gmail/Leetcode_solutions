#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
# Union Find solution
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
    '''
    Use union find to find the edge that causes a cycle
    Keep track of parenthood by parent
    We put the rank in the parent array such that parent of itself is negative and number of children belong to it is  - parent[i]    
    '''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.UF = UnionFindSet(n)
        for a, b in edges:
            if self.UF.find(a - 1) == self.UF.find(b - 1): return [a, b]
            else: self.UF.union(a - 1, b - 1)
        return [-1, -1]
# @lc code=end

