#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List


class Solution:
    '''
    First go through once, remove in num <= 0 and num > n
    Next, add n to each occurrence at the index
    Finally find the first index with # < n
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            if num <= 0 or num > n: nums[i] = 0
        for num in nums:
            if 1 <= num <= n: nums[num - 1] += n
        for i in range(n):
            if not nums[i] // n: return i + 1
        return -1 
        
# @lc code=end

