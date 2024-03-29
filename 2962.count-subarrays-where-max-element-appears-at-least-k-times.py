#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    Find max(nums) first
    Then record appearance of maxNums: appear
    For each i, we binary search right i in appear. If index >= k, appear[index - k] subarrays ending at i satisfy the condition 
    '''
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum, n = max(nums), len(nums)
        appear = []
        result = 0
        for i, num in enumerate(nums):
            if num == maxNum: appear.append(i)
        for i in range(n):
            index = bisect.bisect_right(appear, i)
            if index >= k: result += appear[index - k] + 1
        return result
# @lc code=end

