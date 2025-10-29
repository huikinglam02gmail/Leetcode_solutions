#
# @lc app=leetcode id=3708 lang=python3
#
# [3708] Longest Fibonacci Subarray
#

from typing import List

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        result = 2
        current = 2
        for i in range(2, n):
            if nums[i] == nums[i - 1] + nums[i - 2]: current += 1
            else: current = 2
            result = max(result, current)
        return result
# @lc code=end

