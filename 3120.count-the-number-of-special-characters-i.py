#
# @lc app=leetcode id=3120 lang=python3
#
# [3120] Count the Number of Special Characters I
#

# @lc code=start
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        counts = [[0, 0] for i in range(26)]
        for c in word:
            if c.isupper(): counts[ord(c) - ord('A')][1] += 1
            else: counts[ord(c) - ord('a')][0] += 1
        result = 0
        for i in range(26):
            if counts[i][0] * counts[i][1] > 0: result += 1
        return result
# @lc code=end

