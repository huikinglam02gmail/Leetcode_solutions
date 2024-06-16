#
# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#

# @lc code=start
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reach = 0
        count = 0
        index = 0
        while reach < n:
            if index < len(nums) and nums[index] <= reach + 1:
                reach += nums[index]
                index += 1
            else:
                count += 1
                reach += reach + 1
        return count
            
# @lc code=end

