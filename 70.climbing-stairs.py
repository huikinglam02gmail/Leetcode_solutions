#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    # To reach n, u first need to reach n - 1 or n - 2
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            dp = [0]*n
            dp[0] = 1
            dp[1] = 2
            for i in range(2, n):
                dp[i] += dp[i-1]
                dp[i] += dp[i-2]
            return dp[-1]
# @lc code=end

