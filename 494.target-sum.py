#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for num in nums:
            dpNew = {}
            for key in dp.keys():
                dpNew[key + num] = dpNew.get(key + num, 0) + dp[key]
                dpNew[key - num] = dpNew.get(key - num, 0) + dp[key]
            dp = dpNew
        return dp.get(target, 0)
        
# @lc code=end

