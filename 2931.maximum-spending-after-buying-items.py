#
# @lc app=leetcode id=2931 lang=python3
#
# [2931] Maximum Spending After Buying Items
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        heap = []
        n = len(values[0])
        for i in range(len(values)): heapq.heappush(heap, [values[i][n - 1], i, n - 1])
        result = 0
        d = 1
        while heap:
            val, i, j = heapq.heappop(heap)
            result += val * d
            d += 1
            if j > 0: heapq.heappush(heap, [values[i][j - 1], i, j - 1])
        return result
# @lc code=end

