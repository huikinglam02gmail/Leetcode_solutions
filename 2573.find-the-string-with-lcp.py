#
# @lc app=leetcode id=2573 lang=python3
#
# [2573] Find the String with LCP
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
    The key rule is that if lcp[i][j] > 0, word[i] == word[j]
    And if lcp[i][j] == 0, word[i] != word[j]
    The data structure which would be perfect for this problem is union find. By having each character as a graph node, we unionize different characters with common prefix
    There are a few rules which must be conserved:
    1. lcp[i][j] == lcp[j][i]
    2. lcp[i][j] <= n - max(i, j)
    '''
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        UF = UnionFindSet(n)
        for i in range(n):
            if lcp[i][i] == 0 or lcp[i][i] > n - i:
                return ""
            for j in range(i + 1, n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if lcp[i][j] > n - j:
                    return ""
                if i >= 1 and j >= 1 and lcp[i - 1][j - 1] > 0 and lcp[i][j] != lcp[i - 1][j - 1] - 1:
                    return ""
                if lcp[i][j] > 0:
                    UF.union(i, j)
        
        if UF.count > 26:
            return ""        
        for i in range(n):
            for j in range(i, n):
                if lcp[i][j] == 0 and UF.find(i) == UF.find(j):
                    return ""
                if lcp[i][j] > 0 and UF.find(i) != UF.find(j):
                    return ""
        
        result = ['']*n
        parents = {}
        for i in range(n):
            parent = UF.find(i)
            if parent not in parents:
                parents[parent] = []
            parents[parent].append(i)
        j = 0
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i in range(n):
            if result[i] == '':
                for k in parents[UF.find(i)]:
                    result[k] = alphabets[j]
                j += 1
        return "".join(result)
# @lc code=end