#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0
        n = len(word)
        while i < n and word[i] != ch: i += 1
        return word if i == n else word[i::-1] + word[i + 1:]

# @lc code=end

