#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
from functools import lru_cache


class Solution:
    @lru_cache(None)    
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True       
        for i in range(1,len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[-i:], s2[:i]) and self.isScramble(s1[:-i],s2[i:])):
                return True
        return False
# @lc code=end

