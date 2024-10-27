#
# @lc app=leetcode id=3194 lang=python3
#
# [3194] Minimum Average of Smallest and Largest Elements
#

# @lc code=start
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        result =  float("inf")
        nums.sort()
        for i in range(len(nums) // 2): result = min(result, (nums[i] + nums[len(nums) - 1 - i]) / 2)
        return result
# @lc code=end

