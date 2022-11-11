#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        last, power, result = 'A', 0, 0
        for c in s:
            if c == last:
                power += 1
            else:
                power = 1
            result, last = max(result, power), c
        return result
# @lc code=end

