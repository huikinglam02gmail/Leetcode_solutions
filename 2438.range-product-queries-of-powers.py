#
# @lc app=leetcode id=2438 lang=python3
#
# [2438] Range Product Queries of Powers
#

# @lc code=start
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        binN = bin(n)[2:]
        powers = []
        for i in range(len(binN) - 1, -1, -1):
            if binN[i] == "1": powers.append(1 << (len(binN) - 1 - i))
        
        MOD = 1000000007
        allPossibleResults =  [[0 for i in range(len(powers))] for j in range(len(powers))]
        for i in range(len(powers)):
            for j in range(i, len(powers)):
                if i == j: allPossibleResults[i][j] = powers[i]
                else: 
                    allPossibleResults[i][j] = powers[j] * allPossibleResults[i][j - 1]
                    allPossibleResults[i][j] %= MOD
        result = []
        for a, b in queries: result.append(allPossibleResults[a][b])
        return result
# @lc code=end

