#
# @lc app=leetcode id=2698 lang=python3
#
# [2698] Find the Punishment Number of an Integer
#

# @lc code=start
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def isPun(self, nString):
        if len(nString) == 0:
            return {}
        else:
            result = set()
            result.add(int(nString))
            for cut in range(1, len(nString)):
                for item in self.isPun(nString[cut:]):
                    result.add(int(nString[:cut]) + item)
            return result
    
    def punishmentNumber(self, n: int) -> int:
        result = 0
        for i in range(1, n + 1, 1):
            if i in self.isPun(str(i*i)):
                result += i*i
        return result
# @lc code=end

