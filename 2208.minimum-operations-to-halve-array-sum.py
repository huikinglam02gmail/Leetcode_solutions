#
# @lc app=leetcode id=2208 lang=python3
#
# [2208] Minimum Operations to Halve Array Sum
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    Simulate with a max heap. 
    '''
    def halveArray(self, nums: List[int]) -> int:
        S = 0
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
            S += num
        
        reduced = 0
        steps = 0
        while reduced < (S / 2):
            negNum = heapq.heappop(heap)
            reduced +=  (- negNum) / 2
            heapq.heappush(heap, - ((- negNum) / 2))
            steps += 1
        return steps
        
# @lc code=end

