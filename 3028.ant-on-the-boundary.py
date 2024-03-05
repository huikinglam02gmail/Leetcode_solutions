#
# @lc app=leetcode id=3028 lang=python3
#
# [3028] Ant on the Boundary
#

# @lc code=start
from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        result = 0
        x = 0
        for num in nums:
            x += num
            if x == 0: result += 1
        return result
# @lc code=end

