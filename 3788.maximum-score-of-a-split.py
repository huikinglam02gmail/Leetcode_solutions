#
# @lc app=leetcode id=3788 lang=python3
#
# [3788] Maximum Score of a Split
#

# @lc code=start
from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        prefix = 0
        prefixSum = []
        for num in nums:
            prefix += num
            prefixSum.append(prefix)
        suffixMin = []
        currentMin = float('inf')
        for num in reversed(nums):
            currentMin = min(currentMin, num)
            suffixMin.append(currentMin)
        suffixMin.reverse()
        maxScore = - float('inf')
        for i in range(len(nums) - 1):
            maxScore = max(maxScore, prefixSum[i] - suffixMin[i + 1])
        return maxScore
# @lc code=end

