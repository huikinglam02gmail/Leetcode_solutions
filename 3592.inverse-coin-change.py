#
# @lc app=leetcode id=3592 lang=python3
#
# [3592] Inverse Coin Change
#

# @lc code=start
from typing import List


class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        result = []
        n = len(numWays)
        for i in range(n):
            if numWays[i] == 0: continue
            elif numWays[i] == 1:
                result.append(i + 1)
                for j in range(n - 1, i, -1):
                    if numWays[j] >= numWays[j - i - 1]: numWays[j] -= numWays[j - i - 1]
                    else: return []
                numWays[i] = 0
            else: return []
        return result
# @lc code=end

