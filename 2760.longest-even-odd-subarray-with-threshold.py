#
# @lc app=leetcode id=2760 lang=python3
#
# [2760] Longest Even Odd Subarray With Threshold
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just proceed as described
    '''
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        result = 0
        for i, num in enumerate(nums):
            if num % 2 == 0 and num <= threshold:
                j = i + 1
                while j < n and nums[j] % 2 != nums[j - 1] % 2 and nums[j] <= threshold:
                    j += 1
                result = max(result, j - i)
        return result 
        
# @lc code=end

