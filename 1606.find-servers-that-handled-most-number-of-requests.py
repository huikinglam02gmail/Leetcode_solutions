#
# @lc app=leetcode id=1606 lang=python3
#
# [1606] Find Servers That Handled Most Number of Requests
#

# @lc code=start
import heapq
from typing import List
from sortedcontainers import SortedList


class Solution:
    # keep a heap to maintain finish time
    # keep a sortedlist to keep the free servers
    # For each new arrival and load, get the bisectleft index and pop it out if the free servers sortedlist is not empty
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        usage = [0]*k
        free = SortedList()
        for i in range(k):
            free.add(i)
        busy = []

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                time, ind = heapq.heappop(busy)
                free.add(ind)
            if len(free) > 0:
                ind = free.bisect_left(i % k)
                eleToUse = free[ind % len(free)]
                free.remove(eleToUse)
                heapq.heappush(busy, [arrival[i] + load[i], eleToUse])
                usage[eleToUse] += 1

        result = []
        maxSoFar = 0
        for i, num in enumerate(usage):
            if num > maxSoFar:
                result.clear()
                maxSoFar = num
            if num >= maxSoFar:
                result.append(i)
        return result
        
# @lc code=end

