#
# @lc app=leetcode id=1959 lang=python3
#
# [1959] Minimum Total Space Wasted With K Resizing Operations
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    This is a DP problem. Let dp(i, j) = minimum total space wasted if you can resize the array nums[i:] at most j times.
    We want to get dp(0, k).
    Base case if k = 0, we have to set array size to be max(nums[i:]) and the result is (n - i) * max(nums[i:]) - sum(nums[i:])
    dp(i, j) = min(dp(l, k - 1) - cost(i, l))
    '''

    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        rangeMax = [[0 for j in range(n)] for i in range(n)]
        Cost = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                if j == i:
                    rangeMax[i][j] = nums[i]
                else:
                    rangeMax[i][j] = max(nums[j], rangeMax[i][j - 1])
                Cost[i][j] = (j + 1 - i) * rangeMax[i][j] - prefix[j + 1] + prefix[i]
        
        dp = [[float("inf") for i in range(n)] for j in range(k + 1)]
        for i in range(k + 1):
            for j in range(n - 1, -1 , -1):
                if i == 0:
                    dp[i][j] = Cost[j][n - 1]
                else:
                    for l in range(j + 1, n + 1):
                        if l < n:
                            dp[i][j] = min(dp[i][j], dp[i - 1][l] + Cost[j][l - 1])
                        else:
                            dp[i][j] = min(dp[i][j], Cost[j][l - 1])     

        return dp[k][0]
        
# @lc code=end

