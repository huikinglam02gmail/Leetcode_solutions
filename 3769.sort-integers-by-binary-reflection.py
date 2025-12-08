#
# @lc app=leetcode id=3769 lang=python3
#
# [3769] Sort Integers by Binary Reflection
#

# @lc code=start
from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        reflected = []
        for i, num in enumerate(nums):
            reflected.append([int(bin(num)[2:][::-1], 2), i])
        reflected.sort(key = lambda x: [x[0], nums[x[1]]])
        result = [0] * len(nums)
        for i, item in enumerate(reflected):
            result[i] = nums[item[1]]
        return result

# @lc code=end

