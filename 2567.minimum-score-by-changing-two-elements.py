#
# @lc app=leetcode id=2567 lang=python3
#
# [2567] Minimum Score by Changing Two Elements
#

# @lc code=start
from typing import List


class Solution:
    '''
    Sort
    Then change either top 2, top 1 and bottom 1 or bottom 2
    get minimum of the respective diffs
    '''
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-3] - nums[0], nums[-2] - nums[1], nums[-1] - nums[2])
# @lc code=end

