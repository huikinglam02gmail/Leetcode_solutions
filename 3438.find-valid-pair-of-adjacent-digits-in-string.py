#
# @lc app=leetcode id=3438 lang=python3
#
# [3438] Find Valid Pair of Adjacent Digits in String
#

# @lc code=start
class Solution:
    def findValidPair(self, s: str) -> str:
        counts = [0] * 10
        for c in s: counts[int(c)] += 1
        for i in range(len(s) - 1):
            if s[i] != s[i + 1] and counts[int(s[i])] == int(s[i]) and counts[int(s[i + 1])] == int(s[i + 1]): return s[i:i + 2]
        return ""
# @lc code=end

