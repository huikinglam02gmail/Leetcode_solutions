#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0
        for num in nums:
            if num < 0:
                negatives += 1
            elif num == 0:
                return 0
        return 1 if negatives % 2 == 0 else -1
# @lc code=end

