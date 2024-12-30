#
# @lc app=leetcode id=2202 lang=python3
#
# [2202] Maximize the Topmost Element After K Moves
#

# @lc code=start
from typing import List


class Solution:
    '''
    Different cases:
    1. like example 1: return max(nums[: k - 1]) if k < len(nums)
    2. if len(nums) == 1 and k % 2 > 0: return -1
    '''
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return -1 if k % 2 else nums[0]
        if k < len(nums):
            if k > 1:
                candidate = max(nums[:k - 1])
                return candidate if nums[k] < candidate else nums[k]
            else: return nums[k]
        elif k == len(nums): return max(nums[:k - 1])
        else: return max(nums)
# @lc code=end

