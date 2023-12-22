#
# @lc app=leetcode id=2028 lang=python3
#
# [2028] Find Missing Observations
#

# @lc code=start
from typing import List


class Solution:
    '''
    We are given sum(total) / (m + n) == mean
    so sum(ans) = mean * (m + n) - sum(rolls)
    we return empty array if sum(ans) < n or sum(ans) > 6 * n
    Otherwise we just keep putting sum(ans) // n and fill the rest
    '''
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumAns = mean * (len(rolls) + n) - sum(rolls)
        result = []
        if n <= sumAns <= 6 * n:
            defaultDice = sumAns // n
            result = [0] * n
            for i in range(n):
                result[i] += defaultDice
                sumAns -= defaultDice
            i = 0
            while sumAns > 0:
                result[i] += 1
                sumAns -= 1
                i += 1
        return result
# @lc code=end

