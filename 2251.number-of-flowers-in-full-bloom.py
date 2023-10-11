#
# @lc app=leetcode id=2251 lang=python3
#
# [2251] Number of Flowers in Full Bloom
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    1 <= starti <= endi <= 10^9
    Line Sweep would be too slow
    On the other hand, we can maintain a min heap of end.
    Sort people by arrival time and record its index
    '''
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        peopleByArrival = []
        for i, time in enumerate(people):
            peopleByArrival.append([time, i])
        peopleByArrival.sort()

        flowers.sort()
        endHeap = []

        result = [0] * len(people)
        flowerPtr = 0
        for time, i in peopleByArrival:
            while flowerPtr < len(flowers) and flowers[flowerPtr][0] <= time:
                heapq.heappush(endHeap, flowers[flowerPtr][1])
                flowerPtr += 1
            while endHeap and endHeap[0] < time:
                heapq.heappop(endHeap)
            result[i] = len(endHeap)
        return result

# @lc code=end

