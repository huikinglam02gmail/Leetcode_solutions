#
# @lc app=leetcode id=2558 lang=python3
#
# [2558] Take Gifts From the Richest Pile
#

# @lc code=start
import heapq
from math import isqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts: heapq.heappush(heap, -gift)
        
        for i in range(k):
            num = heapq.heappop(heap)
            heapq.heappush(heap, - isqrt(- num))
        
        return - sum(heap)
            
# @lc code=end

