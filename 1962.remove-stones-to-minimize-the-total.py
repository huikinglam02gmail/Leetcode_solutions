#
# @lc app=leetcode id=1962 lang=python3
#
# [1962] Remove Stones to Minimize the Total
#

# @lc code=start
import heapq
from typing import List


class Solution:
    # clearly a priority queue question
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for pile in piles:
            heapq.heappush(heap, -pile)
        for i in range(k):
            item = - heapq.heappop(heap)
            item -= item // 2
            heapq.heappush(heap, -item)
        return - sum(heap)
# @lc code=end

