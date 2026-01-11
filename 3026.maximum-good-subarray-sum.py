#
# @lc app=leetcode id=3026 lang=python3
#
# [3026] Maximum Good Subarray Sum
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        ending = {}
        ending[nums[0]] = [0]
        result = - float('inf')
        for i, num in enumerate(nums):
            prefix += num
            candidates = [num - k, num + k]
            for candidate in candidates:
                if candidate in ending:
                    result = max(result, prefix - ending[candidate][0])
            if i < len(nums) - 1:
                if nums[i + 1] not in ending:
                    ending[nums[i + 1]] = []
                heapq.heappush(ending[nums[i + 1]], prefix)
        return result if result != - float('inf') else 0

# @lc code=end
