#
# @lc app=leetcode id=1632 lang=python3
#
# [1632] Rank Transform of a Matrix
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
    # We first sort the values in matrix
    # Then we build the graph from small value to large
    # The trick is for a value appearing multiple times in the matrix, 
    # we need to build the disjoint-set structure
    # This structure has m + n elements (m = row number, n = column number)
    # For each element belonging to the value, we union up the corresponding row and col.
    # Then we loop through the rows and columns and assign rankMax[find[i]] = max(rank[find[i]], rank[i])
    # We also record the inverse mapping from find[i] to each i
    # Therefore the find[i] for each cluster should contain the maximum rank for the row-group in each round
    # So update the new rank and assign the result
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        hashTable = {}
        for i in range(m):
            for j in range(n):
                if matrix[i][j] not in hashTable:
                    hashTable[matrix[i][j]] = []
                hashTable[matrix[i][j]].append([i,j])

        result = [[0 for j in range(n)] for i in range(m)]
        rank = [0]* (m + n)
        for value in sorted(hashTable.keys()):
            UF = UnionFindSet(m + n)
            changed = set()
            for x, y in hashTable[value]:
                UF.union(x, y + m)
                changed.add(x)
                changed.add(y + m)
            rankMax = rank.copy()
            for i in changed:
                j = UF.find(i)
                rankMax[j] = max(rankMax[j], rank[i])
            for i in changed:
                rank[i] = rankMax[UF.find(i)] + 1
            for x, y in hashTable[value]:
                result[x][y] = rank[x]
        return result            
# @lc code=end