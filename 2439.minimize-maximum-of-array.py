#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    Binary search for the result, answer must be between max and min of nums
    For each possible value, decrement nums[i] from the right until it is smaller than or equal to the limit
    '''
    def minimizeArrayValue(self, nums: List[int]) -> int:
        l, r, n = min(nums), max(nums), len(nums)
        while l < r:
            mid = l + (r - l) // 2
            i = n - 1
            current = 0
            while i > 0:
                increment = nums[i] + current - mid
                current = max(0, increment)
                i -= 1
            if nums[i] + current > mid:
                l = mid + 1
            else:
                r = mid
        return l
                
        
# @lc code=end

