#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from typing import List


class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target_sum = total // 2
        dp = [[False for i in range(len(nums))] for j in range(target_sum + 1)]
        for i in range(len(nums)): dp[0][i] = True
        for i in range(1, target_sum + 1): dp[i][0] = (nums[0] == i)
        for i in range(1, target_sum + 1):
            for j in range(1, len(nums)):
                dp[i][j] = dp[i][j - 1]
                if i - nums[j] >= 0: dp[i][j] |= dp[i - nums[j]][j - 1]
        return dp[target_sum][len(nums) - 1]
# @lc code=end

