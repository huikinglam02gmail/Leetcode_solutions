#
# @lc app=leetcode id=3798 lang=python3
#
# [3798] Largest Even Number
#

# @lc code=start
class Solution:
    def largestEven(self, s: str) -> str:
        j = len(s) - 1
        while j >= 0 and s[j] != '2': j -= 1
        return s[:j + 1]
        
# @lc code=end

