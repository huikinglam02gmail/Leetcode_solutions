#
# @lc app=leetcode id=1444 lang=python3
#
# [1444] Number of Ways of Cutting a Pizza
#

# @lc code=start
from functools import lru_cache

class Solution:
    # DP problem
    # dp(i,j,c) = Return the number of ways of cutting pizza[i:][j:]
    # such that each piece contains at least one apple and there are c cuts left
    # In order to make sure the pieces after cut has at least one apple
    # We reuse code from 304. Range Sum Query 2D - Immutable that uses prefix sum

    @lru_cache(None)
    def dp(self, i, j, c):
        if c == 0:
            if self.sumRegion(i, j, self.m-1, self.n-1) >= 1:
                return 1
            else:
                return 0
        if self.sumRegion(i, j, self.m-1, self.n-1) == 0:
            return 0
        else:
            result = 0
            for l in range(1, self.m + 1):
                if self.sumRegion(i, j, l-1, self.n-1) >= 1:
                    result += self.dp(l, j, c - 1)
            for l in range(1, self.n + 1):
                if self.sumRegion(i, j, self.m-1, l-1) >= 1:
                    result += self.dp(i, l, c - 1)
            return result                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.P[row2+1][col2+1] - self.P[row1][col2+1] - self.P[row2+1][col1] + self.P[row1][col1]
    
    def ways(self, pizza: List[str], k: int) -> int:
        self.m, self.n, self.MOD = len(pizza), len(pizza[0]), pow(10,9) + 7
        self.P = [[0 for j in range(self.n+1)] for i in range(self.m+1)]
        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                self.P[i][j] = self.P[i-1][j] + self.P[i][j-1] - self.P[i-1][j-1]
                if pizza[i-1][j-1] == 'A':
                    self.P[i][j] += 1
        return self.dp(0,0,k-1) % self.MOD
    
        
# @lc code=end

