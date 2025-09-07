#
# @lc app=leetcode id=3566 lang=python3
#
# [3566] Partition Array into Two Equal Product Subsets
#

# @lc code=start
from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        dp = [1] * (1 << n)
        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):
                    dp[mask] = dp[mask ^ (1 << i)] * nums[i]
                    continue
        for mask in range(1, (1 << n)):
            if dp[mask] == target and dp[((1 << n) - 1) ^ mask] == target:
                return True
        return False
# @lc code=end

