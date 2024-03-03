#
# @lc app=leetcode id=3038 lang=python3
#
# [3038] Maximum Number of Operations With the Same Score I
#

# @lc code=start
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        result = 0
        const = -1
        while i < n - 1:
            if nums[i] + nums[i + 1] != const and const > 0: break
            if const < 0: const = nums[i] + nums[i + 1]
            i += 2
            result += 1
        return result

# @lc code=end

