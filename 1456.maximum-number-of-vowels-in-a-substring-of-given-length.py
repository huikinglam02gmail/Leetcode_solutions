#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        current, result, n = 0, 0, len(s)
        for i in range(k):
            if s[i] in "aeiou":
                current += 1
        result = current
        for i in range(k,n,1):
            if s[i] in "aeiou":
                current += 1
            if s[i-k] in "aeiou":
                current -= 1
            result = max(result, current)
        return result
# @lc code=end

