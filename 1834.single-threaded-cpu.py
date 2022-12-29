#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#

# @lc code=start
import heapq
from typing import List


class Solution:
    # We can first sort tasks according to enqueue time.
    # Then using a global time, push the tasks into a heap
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        data = []
        for i, task in enumerate(tasks):
            data.append([task[1], i, task[0]])
        data.sort(key = lambda x: x[2])

        globalTime, p, n = 0, 0, len(data)
        heap, result = [], []
        while p < n or heap:
            if not heap:
                globalTime = data[p][2]
                while p < n and data[p][2] == globalTime:
                    heapq.heappush(heap, data[p])
                    p += 1
            processingTime, ind, enqueueTime = heapq.heappop(heap)
            globalTime += processingTime
            result.append(ind)
            while p < n and data[p][2] <= globalTime:
                heapq.heappush(heap, data[p])
                p += 1
            
        return result
# @lc code=end
