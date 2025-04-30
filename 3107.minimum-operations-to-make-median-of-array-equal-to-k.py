#
# @lc app=leetcode id=3107 lang=python3
#
# [3107] Minimum Operations to Make Median of Array Equal to K
#

# @lc code=start
from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        for i in range(n // 2, -1, -1):
            if nums[i] > k: 
                result += nums[i] - k
                nums[i] = k
        for i in range(n // 2, n, 1):
            if nums[i] < k: 
                result += k - nums[i]
                nums[i] = k
        return result
# @lc code=end

