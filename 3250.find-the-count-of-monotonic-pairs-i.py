#
# @lc app=leetcode id=3250 lang=python3
#
# [3250] Find the Count of Monotonic Pairs I
#

# @lc code=start
from typing import List


class Solution:
    '''
    Let dp[i][a] by the number of monotonic increasing arr1 of length i + 1 ending with a.
    notice this corresponds to number of monotonic decreasing arr2 of length i + 1 ending with nums[i] - a.
    when we add a new element nums[i + 1], possible ends b are given by:
    0 <= a <= b <= nums[i + 1]
    0 <= nums[i + 1] - b <= nums[i] - a <= nums[i + 1]
    '''
    def countOfPairs(self, nums: List[int]) -> int:
        dp = {}
        MOD = 1000000007
        for i in range(nums[0] + 1): dp[i] = 1
        for i in range(1, len(nums)):
            dpNew = {}
            for a in dp:
                for b in range(a + max(0, nums[i] - nums[i - 1]), nums[i] + 1, 1):
                    dpNew[b] = dpNew.get(b, 0) + dp[a]
                    dpNew[b] %= MOD
            dp = dpNew
        return sum(dp.values()) % MOD
# @lc code=end

