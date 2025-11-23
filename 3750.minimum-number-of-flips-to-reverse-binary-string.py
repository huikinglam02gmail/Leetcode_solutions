#
# @lc app=leetcode id=3750 lang=python3
#
# [3750] Minimum Number of Flips to Reverse Binary String
#

# @lc code=start
class Solution:
    def minimumFlips(self, n: int) -> int:
        bin_str = bin(n)[2:]
        left, right = 0, len(bin_str) - 1
        flips = 0
        while left < right:
            if bin_str[left] != bin_str[right]:
                flips += 2
            left += 1
            right -= 1
        return flips
# @lc code=end

