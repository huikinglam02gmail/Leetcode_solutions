#
# @lc app=leetcode id=3108 lang=python3
#
# [3108] Minimum Cost Walk in Weighted Graph
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
    '''
    If two nodes are not in the same cluster, return -1
    If they are in the same cluster, the minimum cost path is two traverse every edge, as AND of multiple numbers lead to smaller product. 
    '''
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        UF = UnionFindSet(n)
        for u, v, w in edges: UF.union(u, v)

        groupId = []
        for i in range(n): groupId.append(UF.find(i))
        ClusterWeight = {}
        for u, v, w in edges:
            group = UF.find(u)
            if group not in ClusterWeight: ClusterWeight[group] = w
            else: ClusterWeight[group] &= w

        result = []
        for s, t in query:
            if UF.find(s) != UF.find(t): result.append(-1)
            else: result.append(ClusterWeight[UF.find(s)])
        return result
# @lc code=end

