#
# @lc app=leetcode id=3160 lang=python3
#
# [3160] Find the Number of Distinct Colors Among the Balls
#

# @lc code=start
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        numToColorMap = {}
        colors = {}
        result = []
        for x, y in queries: 
            if x in numToColorMap:
                colors[numToColorMap[x]] -= 1
                if colors[numToColorMap[x]] == 0: colors.pop(numToColorMap[x])
            numToColorMap[x] = y
            colors[y] = colors.get(y, 0) + 1
            result.append(len(colors))
        return result

# @lc code=end

