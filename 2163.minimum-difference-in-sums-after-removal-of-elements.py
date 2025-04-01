#
# @lc app=leetcode id=2163 lang=python3
#
# [2163] Minimum Difference in Sums After Removal of Elements
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    The cutting point can only occur between i = n and i = 2 * n
    '''
    def minimumDifference(self, nums: List[int]) -> int:
        maxHeap = []
        minHeap = []
        n = len(nums) // 3
        leftMin = [float("inf") for i in range(n + 1)]
        rightMax = [float("inf") for i in range(n + 1)]
        S = 0
        for i in range(2 * n):
            heapq.heappush(maxHeap, - nums[i])
            S += nums[i]
            while len(maxHeap) > n: S += heapq.heappop(maxHeap)
            if i >= n - 1: leftMin[i - n + 1] = S
        S = 0
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(minHeap, nums[i])
            S += nums[i]
            while len(minHeap) > n: S -= heapq.heappop(minHeap)
            if i <= 2 * n: rightMax[i - n] = S
        result = float("inf")
        for i in range(n + 1): result = min(result, leftMin[i] - rightMax[i])
        return result        
# @lc code=end

