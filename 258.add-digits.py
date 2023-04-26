#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            result = 0
            for c in str(num):
                result += int(c)
            return self.addDigits(result)      
# @lc code=end

