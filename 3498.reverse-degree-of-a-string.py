#
# @lc app=leetcode id=3498 lang=python3
#
# [3498] Reverse Degree of a String
#

# @lc code=start
class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i, c in enumerate(s): result += (26 - ord(c) + ord('a')) * (i + 1)
        return result
# @lc code=end

