#
# @lc app=leetcode id=2765 lang=python3
#
# [2765] Longest Alternating Subarray
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just proceed as instructed
    '''
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        result = 1
        for i in range(n - 1):
            j = i + 1
            p = 0
            while j < n and nums[j] == nums[j - 1] + pow(-1, p):
                p += 1
                j += 1
            if nums[j - 1] == nums[i] or nums[j - 1] == nums[i] + 1:
                result = max(result, j - i)             
        return result if result > 1 else -1
# @lc code=end

