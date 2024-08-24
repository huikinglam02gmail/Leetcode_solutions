#
# @lc app=leetcode id=2104 lang=python3
#
# [2104] Sum of Subarray Ranges
#

# @lc code=start
from typing import List


class Solution:
    '''
    First solve 907
    min -> monotonic increasing stack
    max -> monotonic decreasing stack
    '''
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, dp = [0], [0]
        arr = [-float("inf")] + arr
        result = 0
        for i in range(1, len(arr)):
            while arr[stack[-1]] > arr[i]: stack.pop()
            dp.append(dp[stack[-1]] + (i - stack[-1]) * arr[i])
            stack.append(i)
            result += dp[i]
        return result

    def sumSubarrayMaxs(self, arr: List[int]) -> int:
        stack, dp = [0], [0]
        arr = [float("inf")] + arr
        result = 0
        for i in range(1, len(arr)):
            while arr[stack[-1]] < arr[i]: stack.pop()
            dp.append(dp[stack[-1]] + (i - stack[-1]) * arr[i])
            stack.append(i)
            result += dp[i]
        return result

    def subArrayRanges(self, nums: List[int]) -> int:
        return self.sumSubarrayMaxs(nums) - self.sumSubarrayMins(nums)
# @lc code=end

