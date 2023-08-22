#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            result += chr((columnNumber - 1) % 26 + ord('A'))
            columnNumber -= 1
            columnNumber //= 26
        return result[::-1]
# @lc code=end

