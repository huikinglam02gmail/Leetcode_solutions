#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#

# @lc code=start
from typing import List


class Solution:
    '''
    This is a DP problem
    1 <= arr.length <= 500 -> Can look for n^2 (or nk) algorithms
    dp[i] = largest sum of arr[:i + 1] after partitioning
    subproblem structure: in principle, for each [j:i + 1] subwindow (i - j + 1 <= k), we need to look for the max of dp[j] + (i - j + 1) * max(arr[j:i + 1])
    To do this efficiently, we can use a variable currMax to scan for max seen from arr[i] back to arr[j:i + 1]    
    '''
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            curr_max = 0
            for j in range(i - 1, max(i - k - 1, -1), -1):
                curr_max = max(curr_max, arr[j])
                dp[i] = max(dp[i], dp[j] + (i - j) * curr_max)
        return dp[-1]
# @lc code=end

