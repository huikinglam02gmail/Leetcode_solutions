#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#

# @lc code=start
from typing import List


class Solution:
    '''
    DP problem
    dp[i][j] = size of largest square having (i,j) as bottom right corner
    it will contribute dp[i][j] to the final result
    dp[i][j] = 1 + min(dp[i-1][j], dp[i - 1][j-1], dp[i-1][j])    
    '''
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0
        for i in range(len(matrix)):
            dp = [0 for k in range(len(matrix[0]))]
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[j] = 1
                    if i > 0 and j > 0:
                        dp[j] += min(dp[j-1], dp_prev[j-1], dp_prev[j])
                    result += dp[j]
            dp_prev = dp[:]
        return result
# @lc code=end

