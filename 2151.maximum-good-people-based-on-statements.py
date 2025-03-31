#
# @lc app=leetcode id=2151 lang=python3
#
# [2151] Maximum Good People Based on Statements
#

# @lc code=start
from typing import List


class Solution:
    '''
    Use bitmask to represent possible state of good / bad: 1 = good, 0 = bad
    Since bad might tell either truth or lie, so it doesn't matter
    Only the good ones opinions matter
    '''
    def maximumGood(self, statements: List[List[int]]) -> int:
        self.statements = statements
        result = 0
        for mask in range(1 << len(statements)):
            good = []
            bad = []
            for j in range(len(statements)):
                if (mask & (1 << j)) > 0: good.append(j)
                else: bad.append(j)
            consistent = True
            for i in range(len(good) - 1):
                for j in range(i + 1, len(good)):
                    consistent &= (statements[good[j]][good[i]] >= 1)
                    consistent &= (statements[good[i]][good[j]] >= 1)
            for i in range(len(good)):
                for j in range(len(bad)):
                    consistent &= (statements[good[i]][bad[j]] % 2 == 0) 
            if consistent:
                result = max(result, len(good))
        return result
# @lc code=end

