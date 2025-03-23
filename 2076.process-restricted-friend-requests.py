#
# @lc app=leetcode id=2076 lang=python3
#
# [2076] Process Restricted Friend Requests
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
    Keep union find. For each request, loop through restrictions and ask if the any of the restrictions are broken.
    '''
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        UF = UnionFindSet(n)
        result = []
        for u, v in requests:
            oldParents = UF.parents.copy()
            UF.union(u, v)
            violated = False
            for x, y in restrictions:
                if UF.find(x) == UF.find(y):
                    violated = True
                    break
            if violated: 
                UF.parents = oldParents
                UF.count += 1
                result.append(False)
            else:
                result.append(True)
        return result

        
# @lc code=end

