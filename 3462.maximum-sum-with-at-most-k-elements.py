#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            for j in range(limits[i]):
                heapq.heappush(heap, grid[i][j])
                while len(heap) > k: heapq.heappop(heap)
        result = 0
        while heap: result += heapq.heappop(heap)
        return result
# @lc code=end

