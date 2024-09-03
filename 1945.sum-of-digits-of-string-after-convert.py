#
# @lc app=leetcode id=1945 lang=python3
#
# [1945] Sum of Digits of String After Convert
#

# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ''
        for c in s: string += str(ord(c) - ord('a') + 1)
         
        for i in range(k):
            number = 0
            for c in string: number += int(c)
            string = str(number)
        
        return number
# @lc code=end

