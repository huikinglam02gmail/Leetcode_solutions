#
# @lc app=leetcode id=3736 lang=python3
#
# [3736] Minimum Moves to Equal Array Elements III
#

# @lc code=start
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxNum = max(nums)
        result = 0
        for num in nums:
            result += maxNum - num
        return result
# @lc code=end

