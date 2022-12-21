#
# @lc app=leetcode id=1553 lang=python3
#
# [1553] Minimum Number of Days to Eat N Oranges
#

# @lc code=start
from functools import lru_cache


class Solution:
    # Classic DP problem
    # dp(i) =  minimum number of days to eat i oranges
    # but if we do it according to described (dp(i) = 1 + dp(i-1)) will be too much recursion
    # To avoid that, we simplify by dp(i) = min(i % 3 + dp(i // 3), i % 2 + dp(i // 2))
    # We should notice that 1 is a special case

    @lru_cache(None)
    def dp(self, i):
        if i < 2:
            return i
        else:
            return 1 + min(i % 3 + self.dp(i // 3), i % 2 + self.dp(i // 2))

    def minDays(self, n: int) -> int:
        return self.dp(n)

# @lc code=end

