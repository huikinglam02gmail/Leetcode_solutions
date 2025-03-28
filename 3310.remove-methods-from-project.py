#
# @lc app=leetcode id=3310 lang=python3
#
# [3310] Remove Methods From Project
#

# @lc code=start
from collections import deque
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
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        DirectedGraph = [set() for i in range(n)]
        UF = UnionFindSet(n)

        for a, b in invocations:
            DirectedGraph[a].add(b)
            UF.union(a, b)
        
        suspicious = set()
        dq = deque()
        dq.append(k)
        suspicious.add(k)
        while dq:
            node = dq.popleft()
            for nxt in DirectedGraph[node]:
                if nxt not in suspicious:
                    suspicious.add(nxt)
                    dq.append(nxt)
        
        result = []
        suspiciousList = []
        for i in range(n):
            if UF.find(i) != UF.find(k): result.append(i)
            else: suspiciousList.append(i)
        if len(suspiciousList) == len(suspicious): return result
        else: return result + suspiciousList


# @lc code=end

