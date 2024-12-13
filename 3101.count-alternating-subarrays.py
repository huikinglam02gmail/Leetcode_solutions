#
# @lc app=leetcode id=3101 lang=python3
#
# [3101] Count Alternating Subarrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp[i] = # of alternating subarray ending at i
    '''
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        last = 0
        result = 0
        for i, num in enumerate(nums):
            current = 1
            if i > 0 and nums[i] != nums[i - 1]: current += last
            result += current
            last = current
        return result
            
# @lc code=end

