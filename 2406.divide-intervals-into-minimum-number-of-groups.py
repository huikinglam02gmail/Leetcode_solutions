#
# @lc app=leetcode id=2406 lang=python3
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: [x[0], x[1]])
        result, heap = [], []
        for start, end in intervals:
            if result and heap and heap[0][0] < start:
                last_end, index = heapq.heappop(heap)
                result[index].append([start, end])
                heapq.heappush(heap, [end, index])                
            else:
                result.append([[start, end]])
                heapq.heappush(heap, [end, len(result)-1])
        return len(result)
# @lc code=end

