#
# @lc app=leetcode id=1942 lang=python3
#
# [1942] The Number of the Smallest Unoccupied Chair
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    n == times.length
    2 <= n <= 10^4
    No need to care about infinity. Just keep track of current time and minimum occupied
    '''
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        free = []
        curChair = -1
        timesWithIndex = sorted([[arrival, leaving, i] for i, (arrival, leaving) in enumerate(times)])
        occupied = []
        for arrival, leaving, i in timesWithIndex:
            while occupied and occupied[0][0] <= arrival:
                l, ind = heapq.heappop(occupied)
                heapq.heappush(free, ind)
            if not free:
                curChair += 1
                heapq.heappush(free, curChair)
            freeChairToUse = heapq.heappop(free)
            if i == targetFriend:
                return freeChairToUse
            heapq.heappush(occupied, [leaving, freeChairToUse])
        return -1
            
# @lc code=end

