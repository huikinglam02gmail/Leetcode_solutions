#
# @lc app=leetcode id=3361 lang=python3
#
# [3361] Shift Distance Between Two Strings
#

# @lc code=start
from typing import List


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        dp = [[0 for j in range(26)] for i in range(26)]
        for i in range(26):
            current =  0
            for j in range(25):
                current += nextCost[(i + j) % 26]
                dp[i][(i + j + 1) % 26] = current
        for i in range(26):
            current =  0
            for j in range(25):
                current += previousCost[(i - j + 26) % 26]
                dp[i][(i - j + 25) % 26] = min(dp[i][(i - j + 25) % 26], current)
        
        result = 0
        for c1, c2 in zip(s, t): result += dp[ord(c1) - ord('a')][ord(c2) - ord('a')]
        return result
# @lc code=end

