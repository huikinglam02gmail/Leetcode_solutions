#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Subsequence
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp[i][j] = longest arithmetic subsequence ending at i with difference of j
    dp[i][j] = 1 + dp[i-k][j] if nums[i] - nums[i-k] == j
    To avoid lots of 0s and potential of negative differences, we use a dictionary instead of array to keep the differences    
    '''
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n, dp = len(nums), {}
        for i in range(1, n):
            for k in range(i):
                dp[(i, nums[i] - nums[k])] = 1 + dp.get((k, nums[i] - nums[k]), 1)
        return max(dp.values())
# @lc code=end

