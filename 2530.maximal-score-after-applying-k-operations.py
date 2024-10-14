#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums: heapq.heappush(heap, - num)
        
        score = 0
        for i in range(k):
            num = - heapq.heappop(heap)
            score += num
            newNum = - (num // (-3))
            heapq.heappush(heap, -newNum)
        return score
                           # @lc code=end

