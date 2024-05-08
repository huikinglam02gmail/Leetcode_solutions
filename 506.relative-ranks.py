#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        data = []
        for i, s in enumerate(score): data.append([s, i])
        data.sort(key = lambda x: - x[0])
        n = len(score)
        result = [""] * n
        for i in range(n):
            if i == 0: result[data[i][1]] = "Gold Medal"
            elif i == 1: result[data[i][1]] = "Silver Medal"
            elif i == 2: result[data[i][1]] = "Bronze Medal"
            else: result[data[i][1]] = str(i + 1)
        return result

# @lc code=end

