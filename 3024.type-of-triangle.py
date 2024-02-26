#
# @lc app=leetcode id=3024 lang=python3
#
# [3024] Type of Triangle
#

# @lc code=start
from typing import List


class Solution:
    '''
    two things to check: sort nums, nums[0] + nums[1] > nums[2]
    then ask len(set(num)) = 1 or 2 or 3
    '''
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]: return "none"
        l = len(set(nums))
        if l == 1: return "equilateral"
        if l == 2: return "isosceles"
        if l == 3: return "scalene" 
# @lc code=end

