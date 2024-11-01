#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#

# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3: return s
        else:
            result = ''
            for i in range(len(s) - 2):
                if s[i + 1] != s[i] or s[i + 2] != s[i]: result += s[i]
            result += s[-2] + s[-1]
            return result
# @lc code=end

