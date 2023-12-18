#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
from typing import List


class Solution:
    '''
    The problem can be resolved by dp. Like for [3, 1, 5, 8], we don't really know which one to pop first. 
    How about we switch our thinking and consider which one to pop last? As shown in the case, if 8 is the last one, we know we will get 8 points for sure.
    Similarly, if we decide to pop 1 last, we know we want to get max out of bursting [3] and [5, 8] and add 1 to it.
    Let dp[i][j] = maximum coins you can collect by bursting the balloons nums[i:j + 1], i <= j
    '''
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for x in range(N + 2)] for y in range(N + 2)]

        for j in range(1, N + 1):
            dp[j][j] = nums[j - 1] * nums[j] * nums[j + 1]
            for i in range(j - 1, 0, -1):
                for last in range(i,j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][last - 1] + nums[i - 1]*nums[last]*nums[j + 1] + dp[last + 1][j])
        return dp[1][N]
# @lc code=end

