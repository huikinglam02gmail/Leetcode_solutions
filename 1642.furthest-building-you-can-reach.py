#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    iterate from left to right
    Keep a min heap with size ladder
    Afterwards, bricks -= pop out element    
    '''

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        result = 0
        for i in range(len(heights) - 1):
            if heights[i + 1] > heights[i]:
                heapq.heappush(heap, heights[i + 1] - heights[i])
                if ladders < len(heap):
                    bricks -= heapq.heappop(heap)
                    if bricks < 0:
                        return i
            result = i + 1
        return result
                        
# @lc code=end

