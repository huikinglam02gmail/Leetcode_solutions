#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        nums_set = set(nums)
        p = len(nums) - 1
        while p >= 0 and nums[p] > 0:
            if - nums[p] in nums_set: return nums[p]
            p -= 1
        return -1
        
# @lc code=end

