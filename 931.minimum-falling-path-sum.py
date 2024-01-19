#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
from typing import List


class Solution:
    '''
    DP problem
    dp[i][j] = minimum path sum to arrive at [i,j]
    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) 
    '''
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = []
        for j in range(n):
            dp.append(matrix[0][j])
        for i in range(1,n):
            dpNew = [matrix[i][j] for j in range(n)]
            for j in range(n):
                if j == 0:
                    dpNew[j] += min(dp[j], dp[j+1])
                elif j == n - 1:
                    dpNew[j] += min(dp[j], dp[j-1])
                else:
                    dpNew[j] += min(dp[j-1], dp[j], dp[j+1])
            dp = dpNew
        return min(dp)
# @lc code=end

