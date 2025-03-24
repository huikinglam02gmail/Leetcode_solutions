#
# @lc app=leetcode id=2302 lang=python3
#
# [2302] Count Subarrays With Score Less Than K
#

# @lc code=start
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        S = 0
        result = 0
        for r in range(n):
            S += nums[r]
            while S * (r - l + 1) >= k: 
                S -= nums[l]
                l += 1
            result += r - l + 1
        return result

# @lc code=end

