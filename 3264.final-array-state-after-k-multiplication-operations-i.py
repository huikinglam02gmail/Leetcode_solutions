#
# @lc app=leetcode id=3264 lang=python3
#
# [3264] Final Array State After K Multiplication Operations I
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, num in enumerate(nums): heapq.heappush(heap, [num, i])
        for i in range(k):
            minElement, index = heapq.heappop(heap)
            heapq.heappush(heap, [minElement * multiplier, index])
        while heap:
            element, index = heapq.heappop(heap)
            nums[index] = element
        return nums
# @lc code=end

