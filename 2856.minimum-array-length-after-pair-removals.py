#
# @lc app=leetcode id=2856 lang=python3
#
# [2856] Minimum Array Length After Pair Removals
#

# @lc code=start
from typing import List


class Solution:
    '''
    Basically what's left behind must be numbers occuring > n // 2 times.
    '''
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        maxCount = 1
        count = 1
        for i in range(1, len(nums), 1):
            if nums[i] != nums[i - 1]: count = 1
            else: count += 1
            maxCount = max(maxCount, count)
        return max(len(nums) % 2, maxCount - (len(nums) - maxCount))
        
# @lc code=end

