#
# @lc app=leetcode id=1579 lang=python3
#
# [1579] Remove Max Number of Edges to Keep Graph Fully Traversable
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
    We can collect the edges usable by Alice and Bob respectively
    Then just build the graph from scratch.
    For both cases, use the shared edges first
    We arrive at the minimal necessary skeleton when the size of disjoint set has arrived at n
    The intersection between unused edges by Alice and Bob are those that can be disposed    
    ''' 
    def buildGraph(self, canToss, edges):
        edgeCount = len(edges)
        ind = 0
        while ind < edgeCount:
            if self.DSU.count > 1:
                i, u, v = edges[ind]
                if self.DSU.find(u) == self.DSU.find(v): canToss.add(i)
                else: self.DSU.union(u, v)
            else:
                canToss.add(edges[ind][0])
            ind += 1
        return canToss
    
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        common = []
        Alice = []
        Bob = []
        for i, edge in enumerate(edges):
            t, u, v  = edge
            if t == 1:
                Alice.append([i, u - 1, v - 1])
            elif t == 2:
                Bob.append([i, u - 1, v - 1])
            else:
                common.append([i, u - 1, v - 1])

        canToss = set()
        self.DSU = UnionFindSet(n)
        canToss = self.buildGraph(canToss, common)

        for player in range(2):
            if player == 0:
                specific = Alice
                defaultParents = self.DSU.parents[:]
                defaultCount = self.DSU.count
            else:
                specific = Bob
                self.DSU.parents = defaultParents
                self.DSU.count = defaultCount
            canToss = self.buildGraph(canToss, specific)
            if self.DSU.count > 1: return -1
        return len(canToss)
# @lc code=end

