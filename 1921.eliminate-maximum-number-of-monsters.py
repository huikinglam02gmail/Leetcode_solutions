#
# @lc app=leetcode id=1921 lang=python3
#
# [1921] Eliminate Maximum Number of Monsters
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    Always shoot the monster with shortest arrival time
    '''
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        n = len(dist)
        for i in range(n):
            heapq.heappush(heap, dist[i] / speed[i])
        
        result = 0
        while heap and result < heap[0]:
            heapq.heappop(heap)
            result += 1
        return result
        
# @lc code=end

