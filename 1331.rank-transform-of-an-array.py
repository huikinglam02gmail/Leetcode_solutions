#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#

# @lc code=start
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arrData = [[num, i] for i, num in enumerate(arr)]
        arrData.sort()
        prev = -1000000001
        rank = 0
        result = [0] * len(arr)
        for a, i in arrData:
            if a != prev: rank += 1
            result[i] = rank
            prev = a
        return result
# @lc code=end

