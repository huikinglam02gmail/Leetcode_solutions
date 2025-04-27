#
# @lc app=leetcode id=3532 lang=python3
#
# [3532] Path Existence Queries in a Graph I
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
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        UF = UnionFindSet(n)
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff: UF.union(i, i + 1)
        result = []
        for u, v in queries: result.append(UF.find(u) == UF.find(v))
        return result
# @lc code=end

