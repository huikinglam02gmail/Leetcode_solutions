#
# @lc app=leetcode id=3227 lang=python3
#
# [3227] Vowels Game in a String
#

# @lc code=start
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelCount = 0
        for c in s:
            if c in "aeiou": vowelCount += 1
        return vowelCount > 0
        
# @lc code=end

