#
# @lc app=leetcode id=2680 lang=python3
#
# [2680] Maximum OR
#

# @lc code=start
from typing import List


class Solution:
    '''
    All the shift should be applied to single number
    '''
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [0] * (n + 1)
        right = [0] * (n + 1)
        for i in range(n):
            left[i + 1] = left[i] | nums[i]
            right[n - 1 - i] = right[n - i] | nums[n - 1 - i]
        result = 0
        for i in range(n): result = max(result, left[i] | (nums[i] << k) | right[i + 1])
        return result
# @lc code=end

