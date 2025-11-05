#
# @lc app=leetcode id=3731 lang=python3
#
# [3731] Find Missing Elements
#

# @lc code=start
from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff > 1:
                for j in range(1, diff):
                    result.append(nums[i - 1] + j)
        return result
# @lc code=end

