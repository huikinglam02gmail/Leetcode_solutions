#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use DP to find the winner
    dp[i][j] = maximum score difference between player 1 and player 2 if nums[i:j + 1] is left behind and it's player 1's turn
    '''
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            for i in range(j,-1,-1):
                if i == j: 
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = max(nums[i] - dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][n-1] >= 0
# @lc code=end

