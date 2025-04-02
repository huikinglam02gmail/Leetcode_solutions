#
# @lc app=leetcode id=3275 lang=python3
#
# [3275] K-th Nearest Obstacle Queries
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap = []
        result = []
        for x, y in queries:
            heapq.heappush(heap, - abs(x) - abs(y))
            while len(heap) > k: heapq.heappop(heap)
            if len(heap) == k: result.append(- heap[0])
            else: result.append(-1)
        return result
# @lc code=end

