#
# @lc app=leetcode id=3467 lang=python3
#
# [3467] Transform Array by Parity
#

# @lc code=start
from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted([num % 2 for num in nums])
# @lc code=end

