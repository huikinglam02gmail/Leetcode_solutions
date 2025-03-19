#
# @lc app=leetcode id=3332 lang=python3
#
# [3332] Maximum Points Tourist Can Earn
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp[i][j] = maximum possible points the tourist can earn if he is at i and there are j days left
    '''
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [[0 for j in range(n)] for i in range(k + 1)]
        for j in range(k - 1, -1, -1):
            for i in range(n):
                dp[j][i] = dp[j + 1][i] + stayScore[k - 1 - j][i]
                for l in range(n): dp[j][i] = max(dp[j][i], dp[j + 1][l] + travelScore[l][i])
        return max(dp[0])
# @lc code=end

