#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
import bisect
from typing import List


class Solution:                
    def search(self, nums: List[int], target: int) -> int:
            return target in set(nums)
        
# @lc code=end

