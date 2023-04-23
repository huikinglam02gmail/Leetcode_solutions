#
# @lc app=leetcode id=1416 lang=python3
#
# [1416] Restore The Array
#

# @lc code=start
class Solution:
    '''
    Clearly a DP problem
    dp[i] = the number of the possible arrays that can be printed as s[i:] using the mentioned program. 
    Given 1 <= k <= 10^9, we know the range to search is limited to most 9 digits
    dp[i] = sum(1 + dp[j] if s[i:i+j] < k)    
    '''

    def numberOfArrays(self, s: str, k: int) -> int:
        n, l, MOD = len(s), len(str(k)), pow(10,9) + 7
        dp = [0]*(n + 1)
        dp[n] = 1
        for i in range(n - 1,-1,-1):
            if int(s[i])> 0:
                for j in range(i + 1, 1 + min(n, i + l), 1):
                    if 1 <= int(s[i:j]) <= k:
                        dp[i] += dp[j]
                dp[i] %= MOD
        return dp[0]
# @lc code=end

