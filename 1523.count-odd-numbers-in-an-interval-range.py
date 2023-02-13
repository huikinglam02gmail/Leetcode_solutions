#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = (high - low) // 2
        if low % 2 == 1:
            result += 1
        elif high % 2 == 1:
            result += 1
        return result
# @lc code=end

