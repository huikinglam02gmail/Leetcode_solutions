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
    # The trick is for a value appearing multiple times in the matrix, we need to build the disjoint-set structure
    # and assign the rank of the corresponding row and col + 1 and take the max among the two
    # After going through all elements, we assign the maximum seen of each cluster to each member
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        hashTable = {}
        for i in range(m):
            for j in range(n):
                if matrix[i][j] not in hashTable:
                    hashTable[matrix[i][j]] = []
                hashTable[matrix[i][j]].append([i,j])

        result = [[0 for j in range(n)] for i in range(m)]
        rankX = [0]*m
        rankY = [0]*n
        values = list(hashTable.keys())
        values.sort()
        for value in values:
            l =  len(hashTable[value])
            UF = UnionFindSet(l)
            # get the supposed next value if each element does not interact with others
            rankXTemp = [0] * l
            rankYTemp = [0] * l
            for i in range(l):
                rankXTemp[i] = rankX[hashTable[value][i][0]] + 1
                rankYTemp[i] = rankX[hashTable[value][i][1]] + 1
            if l > 1:
                for i in range(l-1):
                    for j in range(i+1,l):
                        if hashTable[value][i][0] == hashTable[value][j][0] or hashTable[value][i][1] == hashTable[value][j][1]:
                            maxRankXij = max(rankXTemp[UF.find(i)], rankXTemp[UF.find(j)])
                            maxRankYij = max(rankYTemp[UF.find(i)], rankYTemp[UF.find(j)])
                            UF.union(i, j)
                            rankXTemp[UF.find(i)],  rankYTemp[UF.find(j)] = maxRankXij, maxRankYij
            for i in range(l):
                rankX[hashTable[value][i][0]] = max(rankX[hashTable[value][i][0]], rankXTemp[UF.find(i)])
                rankY[hashTable[value][i][1]] = max(rankX[hashTable[value][i][1]], rankYTemp[UF.find(i)])
                result[hashTable[value][i][0]][hashTable[value][i][1]] = max(rankX[hashTable[value][i][0]], rankY[hashTable[value][i][0]])
            print(value, rankX, rankY)                           
        return result            
# @lc code=end

