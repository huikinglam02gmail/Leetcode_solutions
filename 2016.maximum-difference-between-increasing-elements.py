#
# @lc app=leetcode id=2016 lang=python3
#
# [2016] Maximum Difference Between Increasing Elements
#

# @lc code=start
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minSoFar = float('inf')
        result = 0
        for num in nums:
            result = max(result, num - minSoFar)
            minSoFar = min(minSoFar, num)
        return result if result > 0 else -1

# @lc code=end

