#
# @lc app=leetcode id=3362 lang=python3
#
# [3362] Zero Array Transformation III
#

import heapq
from typing import List

# @lc code=start
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        heap = []
        heap2 = []
        queries.sort()
        j = 0
        current = 0
        result = 0
        for i, num in enumerate(nums):
            while heap2 and heap2[0] <= i:
                heapq.heappop(heap2)
                current -= 1
            while j < len(queries) and queries[j][0] <= i:
                heapq.heappush(heap, - queries[j][1])
                j += 1
            while heap and (current < num or i > - heap[0]):
                if i > - heap[0]:
                    heapq.heappop(heap)
                    result += 1
                else:
                    heapq.heappush(heap2, - heapq.heappop(heap) + 1)
                    current += 1
            if current < num: return -1
        return result + len(heap)
# @lc code=end


