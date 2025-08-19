#
# @lc app=leetcode id=3634 lang=python3
#
# [3634] Minimum Removals to Balance Array
#

# @lc code=start
from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        result = float('inf')
        n = len(nums)
        for r in range(n):
            while nums[r] > k * nums[l]: l += 1
            result = min(result, l + n - r - 1)
        return result
# @lc code=end

