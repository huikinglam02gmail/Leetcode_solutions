#
# @lc app=leetcode id=1860 lang=python3
#
# [1860] Incremental Memory Leak
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    0 <= memory1, memory2 <= 2^31 - 1
    ith second allocate i memory
    So it goes as O(sqrt(n)) 
    '''
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        heap = []
        heapq.heappush(heap, [- memory1, 0])
        heapq.heappush(heap, [- memory2, 1])
        i = 1
        while heap[0][0] <= - i:
            negAvailable, ind = heapq.heappop(heap)
            heapq.heappush(heap, [i + negAvailable, ind])
            i += 1
        result = [i, 0, 0]
        while heap:
            negAvailable, ind = heapq.heappop(heap)
            result[ind + 1] = - negAvailable
        return result
        
# @lc code=end

