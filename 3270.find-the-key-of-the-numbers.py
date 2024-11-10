#
# @lc app=leetcode id=3270 lang=python3
#
# [3270] Find the Key of the Numbers
#

# @lc code=start
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        result = 0
        for i in range(4):
            current = num1 % 10
            num1 //= 10
            current = min(current, num2 % 10)
            num2 //= 10
            current = min(current, num3 % 10)
            num3 //= 10 
            result += current * pow(10, i)
        return result
# @lc code=end

