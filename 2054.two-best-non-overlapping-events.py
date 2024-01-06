#
# @lc app=leetcode id=2054 lang=python3
#
# [2054] Two Best Non-Overlapping Events
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    We can sort events by endTime, and put all elements into a min heap of [- value, startTime]
    Then we go through each element. If the heap top start time <= end time, we pop it out
    '''
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[1])
        heap = []
        result = 0
        for s, e, v in events:
            heapq.heappush(heap, [- v, s])
        for s, e, v in events:
            while heap and heap[0][1] <= e:
                heapq.heappop(heap)
            current = 0
            if heap: current -= heap[0][0]
            result = max(result, v + current)
        return result
# @lc code=end

