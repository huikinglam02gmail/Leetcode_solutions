#
# @lc app=leetcode id=1061 lang=python3
#
# [1061] Lexicographically Smallest Equivalent String
#

# @lc code=start
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
    There are 26 nodes
    Each equivalence relation means one edge
    Best way to handle the problem is union find    
    '''

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = UnionFindSet(26)
        n = len(s1)
        for i in range(n): UF.union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        
        resultString = []
        for c in baseStr: resultString.append(chr(UF.find(ord(c) - ord('a')) + ord('a')))
        return ''.join(resultString)
# @lc code=end

