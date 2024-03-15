#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List


class Solution:
    '''
    Scan the array left to right and then back. First we compute the prefix multiplication array starting from the second element
    Then we record cumulative suffix multiplicaiton and scan from n-2 to 0
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1 for i in range(n)]
        
        for i in range(1, n, 1):
            result[i] = result[i - 1] * nums[i - 1]
        last = nums[-1]
        for i in range(n - 2, -1, -1):
            result[i] *= last
            last *= nums[i]
        return result
# @lc code=end

