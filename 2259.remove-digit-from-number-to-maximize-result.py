#
# @lc app=leetcode id=2259 lang=python3
#
# [2259] Remove Digit From Number to Maximize Result
#

# @lc code=start
class Solution:
    '''
    just brute force
    '''
    def removeDigit(self, number: str, digit: str) -> str:
        result = ""
        n = len(number)
        for i in range(n):
            if number[i] == digit: result = max(result, number[:i] + number[i + 1:])
        return result
# @lc code=end

