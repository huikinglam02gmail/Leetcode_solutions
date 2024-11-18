#
# @lc app=leetcode id=3136 lang=python3
#
# [3136] Valid Word
#

# @lc code=start
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        vowelsCount = 0
        consonantCount = 0
        for c in word:
            if not c.isalpha() and not c.isdigit(): return False
            if c.isalpha():
                if c.lower() in 'aeiou': vowelsCount += 1
                else: consonantCount += 1
        return vowelsCount > 0 and consonantCount > 0
            

# @lc code=end

