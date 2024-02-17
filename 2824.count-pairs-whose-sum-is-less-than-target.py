#
# @lc app=leetcode id=2824 lang=python3
#
# [2824] Count Pairs Whose Sum is Less than Target
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    sort and binary search
    '''
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        for i, num in enumerate(nums):
            ind = bisect.bisect_left(nums, target - num)
            result += max(0, ind - i - 1)
        return result
# @lc code=end

