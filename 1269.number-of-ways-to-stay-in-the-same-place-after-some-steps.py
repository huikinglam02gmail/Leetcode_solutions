#
# @lc app=leetcode id=1269 lang=python3
#
# [1269] Number of Ways to Stay in the Same Place After Some Steps
#

# @lc code=start
class Solution:
    '''
    1 <= steps <= 500 and we start from 0 and are only interested in 0, so dp is only up to steps
    Just use hash table    
    '''
    def numWays(self, steps: int, arrLen: int) -> int:
        final_length, MOD = min(steps, arrLen), pow(10, 9) + 7
        dp = [0] * final_length
        dp[0] += 1
        for i in range(steps):
            dp_new = [0] * final_length
            for j in range(final_length):
                dp_new[j] += dp[j]
                dp_new[j] %= MOD
                if j < final_length - 1:
                    dp_new[j + 1] += dp[j]
                    dp_new[j + 1] %= MOD
                if j > 0:
                    dp_new[j - 1] += dp[j]
                    dp_new[j - 1] % MOD
            dp = dp_new
        return dp[0] % MOD
        
# @lc code=end

