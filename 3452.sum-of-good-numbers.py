#
# @lc app=leetcode id=3452 lang=python3
#
# [3452] Sum of Good Numbers
#

# @lc code=start
from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            if (i < k or nums[i] > nums[i - k]) and (i + k >= len(nums) or nums[i] > nums[i + k]): result += nums[i]
        return result
# @lc code=end

