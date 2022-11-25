#
# @lc app=leetcode id=1489 lang=python3
#
# [1489] Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
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
    
# UnionFind + Kruskal
class Solution:
    # An improvement is to identify the critical and pseudocritical edges when we build the MST
    # Instead of finding the final minimum weight and compare by skipping and adding the edge in the MST
    # If we group edges by weight and sort them from small to large:   
    # We notice that the edges can be categorized into three catergories:
    # 1. Redundant: the two vertices of the edge belong to the same parent
    # 2. Critical: skipping this edge would result in increase of 1 in the number of clusters
    # 3. Pseudocritical: skipping this edge would not change the number of clusters

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        Weights = {}
        for i, edge in enumerate(edges):
            if edge[2] not in Weights:
                Weights[edge[2]] = []
            Weights[edge[2]].append([edge[0], edge[1], i])
        DS = UnionFindSet(n)
        critical, pseudo = [], []
        for w in sorted(Weights.keys()):
            nonRedundant = []
            for u, v, i in Weights[w]:
                if DS.find(u) != DS.find(v):
                    nonRedundant.append([u, v, i])
            
            oldParents, oldCount = DS.parents[:], DS.count

            for j in range(len(nonRedundant)):
                for k, (u, v, i) in enumerate(nonRedundant):
                    if k != j:
                        DS.union(u, v)
                countsWithoutJ = DS.count
                DS.union(nonRedundant[j][0], nonRedundant[j][1])
                if DS.count < countsWithoutJ:
                    critical.append(nonRedundant[j][2])
                else:
                    pseudo.append(nonRedundant[j][2])
                DS.parents, DS.count = oldParents[:], oldCount
            
            for (u, v, i) in nonRedundant:
                DS.union(u, v)
        return [critical, pseudo]
                    

# @lc code=end

