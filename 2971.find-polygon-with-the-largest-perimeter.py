#
# @lc app=leetcode id=2971 lang=python3
#
# [2971] Find Polygon With the Largest Perimeter
#

# @lc code=start
from typing import List


class Solution:
    '''
    sort nums
    Then prepare prefix sum array
    Then ask of prefix[i] > nums[i] from back to front
    '''
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        prefix = [0]
        for num in nums: prefix.append(prefix[-1] + num)
        for i in range(n - 1, 0, -1):
            if nums[i] < prefix[i]: return nums[i] + prefix[i]
        return -1
        
# @lc code=end

