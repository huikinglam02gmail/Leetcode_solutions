#
# @lc app=leetcode id=3105 lang=python3
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
#

# @lc code=start
from typing import List


class Solution:
    '''
    Keep track of last num, result so far, current longest strictly increasing and decreasing subarray ending at num
    '''
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        currentIncr, currentDecr, result, n = 1, 1, 1, len(nums)
        for i in range(1, n, 1):
            if nums[i] > nums[i - 1]: currentIncr += 1 
            else: currentIncr = 1
            if nums[i] < nums[i - 1]: currentDecr += 1 
            else: currentDecr = 1
            result = max(result, currentIncr)
            result = max(result, currentDecr)
        return result             
        
# @lc code=end

