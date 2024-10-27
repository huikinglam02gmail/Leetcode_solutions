#
# @lc app=leetcode id=3280 lang=python3
#
# [3280] Convert Date to Binary
#

# @lc code=start
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return bin(int(date[:4]))[2:] + "-" + bin(int(date[5:7]))[2:] + "-" + bin(int(date[8:10]))[2:]
# @lc code=end

