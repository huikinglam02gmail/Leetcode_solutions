#
# @lc app=leetcode id=2222 lang=python3
#
# [2222] Number of Ways to Select Buildings
#

# @lc code=start
class Solution:
    '''
    Only possibilities: "010" and "101"
    Therefore we record # of "10", "01","1" and "0" occurred before s[i]
    dp[] = [count 0, count 1, count 10, count 01]
    '''
    def numberOfWays(self, s: str) -> int:
        dp = [0, 0, 0, 0]
        result = 0
        for c in s:
            if c == "0":
                result += dp[1]
                dp[0] += dp[2]
                dp[3] += 1
            else:
                result += dp[0]
                dp[1] += dp[3]
                dp[2] += 1
        return result
# @lc code=end

