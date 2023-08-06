#
# @lc app=leetcode id=920 lang=python3
#
# [920] Number of Music Playlists
#

# @lc code=start
# Combinatorics solution
from functools import lru_cache
import math


class Solution:
    '''
    DP solution
    dp[i][j] = number of possible playlists that you can create with i songs playlist and j different songs, subjected to the k other songs played before repeat condition
    dp[0][0] = 1
    dp[i][j] = 0 if i < j
    dp[i][j] += dp[i - 1][j - 1] * (n - j + 1)
    dp[i][j] += dp[i - 1][j] * max(j - k, 0)
    '''
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = pow(10, 9) + 7
        dp = [[0 for j in range(n + 1)] for i in range(goal + 1)]
        dp[0][0] = 1
        for j in range(n + 1):
            for i in range(j, goal + 1, 1):
                if i > 0 and j > 0:
                    dp[i][j] += dp[i - 1][j - 1] * (n - j + 1)
                    dp[i][j] %= MOD
                if i > 0:
                    dp[i][j] += dp[i - 1][j] * max(j - k, 0)
                    dp[i][j] %= MOD
        return dp[goal][n]        
# @lc code=end

