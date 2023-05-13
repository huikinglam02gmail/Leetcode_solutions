#
# @lc app=leetcode id=2466 lang=python3
#
# [2466] Count Ways To Build Good Strings
#

# @lc code=start
class Solution:
    '''
    Clearly a DP problem. 
    dp[i] = number of different good strings of length i
    dp[i + zero] += dp[i]
    dp[i + one] += dp[i] 
    '''
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[zero] += 1
        dp[one] += 1
        MOD = pow(10, 9) + 7
        result = 0
        for i in range(min(zero, one), high + 1, 1):
            if i + zero < high + 1:
                dp[i + zero] += dp[i]
                dp[i + zero] %= MOD 
            if i + one < high + 1:
                dp[i + one] += dp[i]
                dp[i + one] %= MOD 
            if low <=  i <= high:
                result += dp[i]
                result %= MOD
        
        return result
# @lc code=end

