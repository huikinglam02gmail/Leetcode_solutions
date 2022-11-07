#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    # The first digit from left with 6 to 9 
    def maximum69Number (self, num: int) -> int:
        num_digit = str(num)
        for i in range(len(num_digit)):
            if num_digit[i] == "6":
                return int(num_digit[:i] + "9" + num_digit[i+1:])
        return num
# @lc code=end

