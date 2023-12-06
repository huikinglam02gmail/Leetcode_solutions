#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days, result = n // 7, n % 7, 0
        for i in range(weeks):
            result += 28 + i * 7
        for i in range(days):
            result += (i + 1) + weeks
        return result
        
# @lc code=end

