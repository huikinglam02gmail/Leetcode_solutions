#
# @lc app=leetcode id=2233 lang=python3
#
# [2233] Maximum Product After K Increments
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    if x < y, (x + 1) * y - x * (y + 1) = y - x > 0
    Therefore we should increment the minimum ones
    '''
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums: heapq.heappush(heap, num)
        while k  > 0:
            num = heapq.heappop(heap)
            heapq.heappush(heap, num + 1)
            k -= 1
        result = 1
        MOD = 1000000007
        while heap:
            result *= heapq.heappop(heap)
            result %= MOD 
        return result

# @lc code=end

