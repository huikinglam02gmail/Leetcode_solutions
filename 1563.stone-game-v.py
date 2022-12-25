#
# @lc app=leetcode id=1563 lang=python3
#
# [1563] Stone Game V
#

# @lc code=start
from typing import List

class Solution:
    # O(n^3) is easy to come up with
    # Here we introduce an O(n^2) algorithm with bottom-up DP
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[0 for i in range(n)] for j in range(n)]
        score = [[0 for i in range(n)] for j in range(n)]

        for j in range(n):
            mid, S, rightHalf = j, 0, 0
            for i in range(j, -1, -1):
                S += stoneValue[i]
                if (i == j):
                    score[i][j] = stoneValue[i]
                else:
                    while (rightHalf + stoneValue[mid])*2 <= S:
                        rightHalf += stoneValue[mid]
                        mid -= 1
                    if 2*rightHalf == S:
                        dp[i][j] = score[i][mid] # get the left half
                    elif mid != i:
                        dp[i][j] = score[i][mid-1]
                    if mid != j:
                        dp[i][j] = max(dp[i][j], score[j][mid + 1]) # get the right half
                    score[i][j] = max(score[i][j-1], dp[i][j] + S)
                    score[j][i] = max(score[j][i+1], dp[i][j] + S)
        return dp[0][n-1]
       
# @lc code=end
