#
# @lc app=leetcode id=1792 lang=python3
#
# [1792] Maximum Average Pass Ratio
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    For each extra student, give to the class with the most amount of potential increase
    '''
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        n = len(classes)
        for p, t in classes:
            heapq.heappush(heap, [p / t - (p + 1) / (t + 1), p, t])

        for j in range(extraStudents, 0, -1):
            r, p, t = heapq.heappop(heap)
            heapq.heappush(heap, [(p + 1) / (t + 1) - (p + 2) / (t + 2), p + 1, t + 1])
        result = 0
        while heap:
            r, p, t = heapq.heappop(heap)
            result +=  p / t
        return result / n
        
# @lc code=end

