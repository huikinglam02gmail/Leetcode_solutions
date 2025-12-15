#
# @lc app=leetcode id=2915 lang=python3
#
# [2915] Length of the Longest Subsequence That Sums to Target
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = {}
        for num in nums:
            dpNew = dp.copy()
            for t in dp:
                if t + num <= target:
                    dpNew[t + num] = max(dpNew.get(t + num, 0), dp[t] + 1)
            if num not in dpNew:
                dpNew[num] = 1
            dp = dpNew
        return dp.get(target, -1)
# @lc code=end
