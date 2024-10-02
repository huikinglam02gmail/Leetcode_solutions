#
# @lc app=leetcode id=2207 lang=python3
#
# [2207] Maximize Number of Subsequences in a String
#

# @lc code=start
class Solution:
    '''
    Since there are only two characters, we either:
    1. put pattern[0] before text
    2. put pattern[1] after text
    and return the max of # of subsequence
    '''
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        result = 0
        counts = 1
        current = 0
        for c in text:
            if c == pattern[1]: current += counts
            if c == pattern[0]: counts += 1
        result = max(result, current)
        counts = 0
        current = 0
        for c in text:
            if c == pattern[1]: current += counts
            if c == pattern[0]: counts += 1
        current += counts
        result = max(result, current)
        return result      
# @lc code=end

