#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    Maintain a max heap and keep popping out two stones at a time   
    '''    
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, - stone)
        
        while len(heap) > 1:
            stone1 = - heapq.heappop(heap)
            stone2 = - heapq.heappop(heap)
            if stone1 > stone2:
                heapq.heappush(heap, stone2 - stone1)
        if len(heap) == 0:
            return 0
        else:
            return -heap[0]
        
# @lc code=end

