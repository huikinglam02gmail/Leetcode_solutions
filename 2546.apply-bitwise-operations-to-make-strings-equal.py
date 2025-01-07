#
# @lc app=leetcode id=2546 lang=python3
#
# [2546] Apply Bitwise Operations to Make Strings Equal
#

# @lc code=start
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        sCount = s.count('1')
        tCount = target.count('1')
        return sCount == tCount or sCount * tCount > 0
# @lc code=end

