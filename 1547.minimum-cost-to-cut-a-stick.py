#
# @lc app=leetcode id=1547 lang=python3
#
# [1547] Minimum Cost to Cut a Stick
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    A classic DP problem. Add 0 and n to cuts
    Sort cuts to faciliate labelling and extraction of length
    So let dp[i][j] = minimum total cost to cut the stick between i and j
    We are looking for dp[0][l], l = len(cut)
    As long as i != j - 1, we can look for the minimum of cuts[j] - cuts[i] + min(dp[i][k] + dp[k][j]), i < k < j   
    '''


    @lru_cache(None)
    def dp(self, i, j):
        if i == j - 1:
            return 0
        result = self.cuts[j] - self.cuts[i]
        extra = float('Inf')
        for k in range(i + 1, j):
            extra = min(extra, self.dp(i, k) + self.dp(k, j))
        return result + extra 
    
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.cuts = [0] + sorted(cuts) + [n]
        return self.dp(0, len(self.cuts)-1)
# @lc code=end

