#
# @lc app=leetcode id=3813 lang=python3
#
# [3813] Vowel-Consonant Score
#

# @lc code=start
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v, c = 0, 0
        for ch in s:
            if ch in 'aeiou':
                v += 1
            elif ch.isalpha():
                c += 1
        if c == 0: return 0
        else: return v // c
# @lc code=end

