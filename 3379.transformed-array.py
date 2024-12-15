#
# @lc app=leetcode id=3379 lang=python3
#
# [3379] Transformed Array
#

# @lc code=start
from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] == 0: result.append(nums[i])
            elif nums[i] > 0: result.append(nums[(i + nums[i]) % len(nums)])
            else:
                j = i + nums[i]
                while j < 0: j += len(nums)
                result.append(nums[j])
        return result
# @lc code=end

