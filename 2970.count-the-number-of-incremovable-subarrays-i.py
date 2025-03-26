#
# @lc app=leetcode id=2970 lang=python3
#
# [2970] Count the Number of Incremovable Subarrays I
#

# @lc code=start
from typing import List


class Solution:
    '''
    Only one subarray is removed each time.
    Keep the left prefix and right suffix arrays. Count the number of strictly increasing subarray that can be formed:
    1. From left elements only
    2. From right elements only
    3. From both left and right
    4. The empty array
    '''
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n - 1 and nums[i] < nums[i + 1]: i += 1
        if i == n - 1: return n * (n + 1) // 2
        j = n - 1
        while j > 0 and nums[j - 1] < nums[j]: j -= 1
        result = n + i - j + 2
        j1 = n - 1
        while i >= 0 and j1 >= j:
            if nums[i] < nums[j1]:
                result += i + 1
                j1 -= 1
            else: i -= 1
        return result

        
# @lc code=end

