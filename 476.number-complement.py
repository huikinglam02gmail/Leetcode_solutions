#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num: i <<= 1
        return (i - 1) ^ num
        
# @lc code=end

