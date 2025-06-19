#
# @lc app=leetcode id=2294 lang=python3
#
# [2294] Partition Array Such That Maximum Difference Is K
#

from typing import List
# @lc code=start
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        curr_min = nums[0] - k - 1
        for i, num in enumerate(nums):
            if num - curr_min > k:# too much
                result += 1
                curr_min = num
        return result
# @lc code=end

