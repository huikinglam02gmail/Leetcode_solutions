#
# @lc app=leetcode id=2730 lang=python3
#
# [2730] Find the Longest Semi-Repetitive Substring
#

# @lc code=start
class Solution:
    '''
    sliding window
    '''
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        current = 0
        l = -1
        result  = 0
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                current += 1
                while l < len(s) and current > 1:
                    l += 1
                    if s[l + 1] == s[l]: current -= 1
            result = max(result, i - l)
        return result

# @lc code=end

