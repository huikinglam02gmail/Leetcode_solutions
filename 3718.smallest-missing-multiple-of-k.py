#
# @lc app=leetcode id=3718 lang=python3
#
# [3718] Smallest Missing Multiple of K
#

# @lc code=start
from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numSet  = set(nums)
        result = k
        while result in numSet:
            result += k
        return result
# @lc code=end

