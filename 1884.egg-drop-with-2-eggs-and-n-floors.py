#
# @lc app=leetcode id=1884 lang=python3
#
# [1884] Egg Drop With 2 Eggs and N Floors
#

# @lc code=start
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1) for i in range(n + 1)]
        for m in range(1, n + 1):
            for K in range(1, k + 1):
                dp[m][K] = dp[m - 1][K - 1] + dp[m - 1][K] + 1
            if dp[m][k] >= n:
                return m
    def twoEggDrop(self, n: int) -> int:
        return self.superEggDrop(2, n)
        
# @lc code=end

