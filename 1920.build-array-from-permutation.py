#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]
# @lc code=end

