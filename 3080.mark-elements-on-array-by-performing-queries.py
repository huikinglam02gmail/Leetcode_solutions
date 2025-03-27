#
# @lc app=leetcode id=3080 lang=python3
#
# [3080] Mark Elements on Array by Performing Queries
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap = []
        S = 0
        for i, num in enumerate(nums): 
            heapq.heappush(heap, [num, i])
            S += num
        result = []
        marked = [False for i in range(len(nums))]
        for index, k in queries:
            if not marked[index]: 
                marked[index] = True
                S -= nums[index]
            k1 = k
            while k1 > 0 and heap:
                num, i = heapq.heappop(heap)
                if not marked[i]:
                    k1 -= 1
                    marked[i] = True
                    S -= nums[i]
            result.append(S)
        return result




# @lc code=end

