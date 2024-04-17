#
# @lc app=leetcode id=3110 lang=python3
#
# [3110] Score of a String
#

# @lc code=start
class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(n - 1): result += abs(ord(s[i + 1]) - ord(s[i]))
        return result
# @lc code=end

