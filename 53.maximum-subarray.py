#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    # Kadane's algorithm
    def maxSubArray(self, nums: List[int]) -> int:      
        max_so_far = - float('inf')
        max_ending_here, n = 0, len(nums)
        
        for num in nums:
            max_ending_here += num
            max_so_far = max(max_so_far, max_ending_here)
            max_ending_here = max(0,max_ending_here)
        return max_so_far
# @lc code=end

