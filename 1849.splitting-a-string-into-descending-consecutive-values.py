#
# @lc app=leetcode id=1849 lang=python3
#
# [1849] Splitting a String Into Descending Consecutive Values
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    1 <= s.length <= 20
    backtracking should be good.
    '''
    @lru_cache(None)
    def backtracking(self, start, end, inFront):
        if inFront > 0 and int(self.s[start:end + 1]) == inFront - 1:
            return True 
        for i in range(start + 1, end + 1):
            if (inFront < 0 or inFront - 1 == int(self.s[start:i])) and self.backtracking(i, end, int(self.s[start:i])):
                return True
        return False

    def splitString(self, s: str) -> bool:
        self.s = s
        n = len(self.s)
        return self.backtracking(0, n - 1, -1)
# @lc code=end

