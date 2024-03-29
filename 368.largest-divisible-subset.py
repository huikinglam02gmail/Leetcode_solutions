#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[i]) < len(dp[j]) + 1:
                        dp[i] = dp[j] + [nums[i]]
        index = 0
        max_length = 1
        for i, item in enumerate(dp):
            if len(item) > max_length:
                index = i
                max_length = len(item)
        return dp[index]
# @lc code=end

