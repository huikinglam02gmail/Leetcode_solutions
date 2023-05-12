#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
from typing import List


class Solution:
    '''
    A DP question. Let dp[i] = max point I can get given questions[i:]
    dp[i] = max(questions[i][0] + dp[i + 1 + questions[i][1]], dp[i + 1])
    '''
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*n
        for i in range(n - 1, -1, -1):
            dp[i] = questions[i][0]
            if i + 1 + questions[i][1] < n:
                dp[i] += dp[i + 1 + questions[i][1]]
            if i < n - 1:
                dp[i] = max(dp[i], dp[i + 1])
        return dp[0]
# @lc code=end

