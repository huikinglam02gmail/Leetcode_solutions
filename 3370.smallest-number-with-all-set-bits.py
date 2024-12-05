#
# @lc app=leetcode id=3370 lang=python3
#
# [3370] Smallest Number With All Set Bits
#

# @lc code=start
class Solution:
    def smallestNumber(self, n: int) -> int:
        num = "1"
        while int(num, 2) < n: num += "1"
        return int(num, 2)
# @lc code=end

