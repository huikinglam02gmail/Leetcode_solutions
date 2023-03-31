#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#

# @lc code=start
from typing import List


class Solution:
    '''
    shrink both sides towards the median gives the minimum move   
    '''
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        result = 0
        while l < r:
            result += nums[r] - nums[l]
            l += 1
            r -= 1
        return result
# @lc code=end

