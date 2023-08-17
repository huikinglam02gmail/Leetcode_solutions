#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    The problem would be much easier if queries and intervals are SORTED
    For each query, we want to get the minimum length VALID interval.
    So, we first get all intervals with start point <= query, and push into a min heap with the interval size as priority and end point as element
    Then, remove invalid shortest interval with end point already past query
    The top will be the answer; if the heap is empty, the answer is -1
    '''
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = sorted([[q, i] for i, q in enumerate(queries)])
        intervals.sort()
        heap = []
        result = [-1] * len(queries)
        i = 0
        for q, ind in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, [intervals[i][1] - intervals[i][0] + 1, intervals[i][1]])
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                result[ind] = heap[0][0]
        return result
        
# @lc code=end

