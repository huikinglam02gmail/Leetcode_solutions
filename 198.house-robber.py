#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    # DP problem
    # recurrence relation quite simple: dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        else:
            dp = [0 for i in range(n)]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n, 1):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp[n-1]
# @lc code=end

