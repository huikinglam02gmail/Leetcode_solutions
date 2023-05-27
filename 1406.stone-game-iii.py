#
# @lc app=leetcode id=1406 lang=python3
#
# [1406] Stone Game III
#

# @lc code=start
from typing import List


class Solution:
    '''
    DP + Game theory problem
    Basically Alice will try to maximize the score and Bob doing the opposite
    dp[i][0] = maximum score Alice can get if only dp[i:] is left behind and it's Alice's turn
    dp[i][1] = maximum score Alice can get if only dp[i:] is left behind and it's Bob's turn
    dp[i][0] = max(stoneValue[i+1] + dp[i+1][1], stoneValue[i+1] + stoneValue[i+2] + dp[i+2][1], stoneValue[i+1] + stoneValue[i+2] + stoneValue[i+3] + dp[i+3][1])
    dp[i][1] = min(dp[i+1][0], dp[i+2][0], dp[i+3][0])
    We want to know if dp[0][0] > sum(stoneValue) // 2   
    '''
    
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        total, n = sum(stoneValue), len(stoneValue)
        dp = [[- float('Inf') if j == 0 else float('Inf') for j in range(2)] for i in range(n)]
        for i in range(n-1,-1,-1):
            current = 0
            for j in range(i, i+3, 1):
                if j < n:
                    current += stoneValue[j]
                    if j + 1 < n:
                        dp[i][0] = max(dp[i][0], current + dp[j+1][1])
                        dp[i][1] = min(dp[i][1], dp[j+1][0])
                    else:
                        dp[i][0] = max(dp[i][0], current)
                        dp[i][1] = min(dp[i][1], 0)
        if dp[0][0] == total / 2:
            return "Tie"
        elif dp[0][0] > total / 2:
            return "Alice"
        else:
            return "Bob"
# @lc code=end

