#
# @lc app=leetcode id=3010 lang=python3
#
# [3010] Divide an Array Into Subarrays With Minimum Cost I
#

# @lc code=start
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        newNums = sorted(nums[1:])
        return nums[0] + newNums[0] + newNums[1]
# @lc code=end

