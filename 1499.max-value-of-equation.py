#
# @lc app=leetcode id=1499 lang=python3
#
# [1499] Max Value of Equation
#

# @lc code=start
import heapq


class Solution:
    # as points is already sorted in x, and new xi must be larger than previously seen xj
    # Then we are interested in knowing the largest yj + yi + (xi - xj) seen
    # yi + xi + (yj - xj)
    # Therefore, for each new (xi, yi), we look for maximum (yj - xj), and keep track for xj
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []
        result = -float('inf')
        for x, y in points:
            while heap and x - heap[0][1] > k:
                heapq.heappop(heap)
            if heap:
                result = max(result, x + y - heap[0][0])
            heapq.heappush(heap, [x - y, x])
        return result
# @lc code=end

