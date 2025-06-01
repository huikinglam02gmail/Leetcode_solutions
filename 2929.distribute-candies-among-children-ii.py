#
# @lc app=leetcode id=2929 lang=python3
#
# [2929] Distribute Candies Among Children II
#

# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for i in range(limit + 1): result += max(0, min(limit, n - i) - max(0, n - i - limit) + 1)
        return result
# @lc code=end

