#
# @lc app=leetcode id=3833 lang=python3
#
# [3833] Count Dominant Indices
#

# @lc code=start
from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        result = 0
        S = nums[-1]
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if (n - 1 - i) * nums[i] > S : result += 1
            S += nums[i]
        return result
# @lc code=end

