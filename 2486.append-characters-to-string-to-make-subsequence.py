#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ps, pt = 0, 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
            else:
                ps += 1
        return len(t) - pt
# @lc code=end

