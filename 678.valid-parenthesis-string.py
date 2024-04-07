#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_max = 0
        open_min = 0
        for c in s:
            if c == "(":
                open_max += 1
                open_min += 1
            if c == ")":
                open_max -= 1
                open_min -= 1
            if c == "*":
                open_max += 1
                open_min -= 1
            if open_max < 0:
                return False
            open_min = max(0, open_min)
        return open_min == 0
        
# @lc code=end

