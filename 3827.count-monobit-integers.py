#
# @lc app=leetcode id=3827 lang=python3
#
# [3827] Count Monobit Integers
#

# @lc code=start
class Solution:
    def countMonobit(self, n: int) -> int:
        result = 1
        current = 1
        while current <= n:
            result += 1
            current *= 2
            current += 1
        return result
# @lc code=end

