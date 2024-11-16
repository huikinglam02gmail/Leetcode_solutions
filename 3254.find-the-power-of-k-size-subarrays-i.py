#
# @lc app=leetcode id=3254 lang=python3
#
# [3254] Find the Power of K-Size Subarrays I
#

# @lc code=start
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = 0
        result = []
        for r in range(len(nums)):
            if r - l + 1 > k: l += 1
            if r > 0 and nums[r] != nums[r - 1] + 1: l = r
            if r - l + 1 == k: result.append(nums[r])
            else: result.append(-1)
        return result[k - 1:]
        
# @lc code=end

