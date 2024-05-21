#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (1 << n)
        j = 0
        for i in range(1, 1 << n):
            if i == (1 << (j + 1)): j += 1             
            dp[i] = dp[i - (1 << j)] ^ nums[j]           
        return sum(dp)
# @lc code=end

