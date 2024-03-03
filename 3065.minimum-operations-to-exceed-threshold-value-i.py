#
# @lc app=leetcode id=3065 lang=python3
#
# [3065] Minimum Operations to Exceed Threshold Value I
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        return bisect.bisect_left(nums, k)
# @lc code=end

