#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
import bisect


class Solution:
    '''
    it could only be XYX. So record the indices. To get palindrome starting and ending with X, len(X) > 1. Then see if they enclose other alphabets between the front and end
    '''
    def countPalindromicSubsequence(self, s: str) -> int:
        occur = [[] for i in range(26)]
        for i, c in enumerate(s):
            occur[ord(c) - ord('a')].append(i)
        result = 0
        for i in range(26):
            if len(occur[i]) > 1:
                for j in range(26):
                    if bisect.bisect_left(occur[j], occur[i][-1]) != bisect.bisect_right(occur[j], occur[i][0]):
                        result += 1
        return result
# @lc code=end

