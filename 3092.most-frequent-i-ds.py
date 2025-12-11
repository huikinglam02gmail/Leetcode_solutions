#
# @lc app=leetcode id=3092 lang=python3
#
# [3092] Most Frequent IDs
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        occur = {}
        result = []
        heap = []
        for num, f in zip(nums, freq):
            if num not in occur:
                occur[num] = 0
            occur[num] += f
            heapq.heappush(heap, (-occur[num], num))
            while heap and occur[heap[0][1]] != -heap[0][0]:
                heapq.heappop(heap)
            result.append(- heap[0][0])
        return result
# @lc code=end

