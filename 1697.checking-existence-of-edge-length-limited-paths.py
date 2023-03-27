#
# @lc app=leetcode id=1697 lang=python3
#
# [1697] Checking Existence of Edge Length Limited Paths
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
    This problem is going to be solved by Union Find. The trick is to first sort the inputs
    We sort queries and edgeList according to distance. At the each query, we build the graph until the edgeList weight is larger than that of query weight. Then we ask if two points are in the same group
    '''
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queriesWithIndicies = sorted([[d, a, b, i] for i, [a, b, d] in enumerate(queries)])
        edgeList.sort(key = lambda x: x[2])

        UF = UnionFindSet(n)
        i, j, m, p = 0, 0, len(queries), len(edgeList)
        result = []
        while i < m and j < p:
            if (queriesWithIndicies[i][0] <= edgeList[j][2]):
                result.append([UF.find(queriesWithIndicies[i][1]) == UF.find(queriesWithIndicies[i][2]), queriesWithIndicies[i][3]])
                i += 1
            else:
                UF.union(edgeList[j][0], edgeList[j][1])
                j += 1
        while i < m:
            result.append([UF.find(queriesWithIndicies[i][1]) == UF.find(queriesWithIndicies[i][2]), queriesWithIndicies[i][3]])
            i += 1
        result = [x[0] for x in sorted(result, key = lambda y: y[1])]
        return result
            

# @lc code=end
