#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        result = []
        while nums:
            result.append(heapq.heappop(nums))
        return result
# @lc code=end

