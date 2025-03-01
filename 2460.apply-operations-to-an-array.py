#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#

# @lc code=start
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                nums[i]*= 2
                nums[i+1] = 0
        result = [0]*n
        j = 0
        for i in range(n):
            if nums[i] != 0:
                result[j] = nums[i]
                j += 1
        return result
# @lc code=end

