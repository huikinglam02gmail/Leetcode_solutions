#
# @lc app=leetcode id=1627 lang=python3
#
# [1627] Graph Connectivity With Threshold
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
    # Build the graph from i = threshold + 1 by multiplying 2*i, 3*i,..., until it reaches n
    # We only need to multiply the primes.
    # We then build the disjoint set and handle the queries

    def getPrimes(self, n):
        primeList = []
        if n >= 2:
            prime = [True]*n
            prime[0] = False
            prime[1] = False
            i = 2
            while i < n:
                if prime[i]:
                    prime[i*i:n:i] = [False]*((n-1-i*i)//i + 1)
                    primeList.append(i)
                i += 1
        return primeList

    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        ListOfPrimes = self.getPrimes(n + 1)
        UF = UnionFindSet(n + 1)
        for node in range(threshold + 1, n + 1, 1):
            j = 0
            while j < len(ListOfPrimes) and ListOfPrimes[j]*node <= n:
                UF.union(node, ListOfPrimes[j]*node)
                j += 1

        result = []
        for a, b in queries:
            result.append(UF.find(a) == UF.find(b))
        return result
# @lc code=end

