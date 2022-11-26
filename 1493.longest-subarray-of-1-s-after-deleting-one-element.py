#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
from typing import List


class Solution:
    # Keep a sliding window which contains at most 1 0
    # Number of consecutive 1 if delete 1 element is then j - i
    def longestSubarray(self, nums: List[int]) -> int:
        left, result, numZeros, n = 0, 0, 0, len(nums)
        for right in range(n):
            if nums[right] == 0:
                numZeros += 1
            while numZeros > 1:
                if nums[left] == 0:
                    numZeros -= 1
                left += 1
            result = max(result, right - left)
        return result

        
# @lc code=end

