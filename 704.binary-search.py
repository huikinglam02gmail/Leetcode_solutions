#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        return -1 if index == len(nums) or nums[index] != target else index 
# @lc code=end

