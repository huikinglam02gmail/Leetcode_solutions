#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    sort and bisect left
    '''
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if n - bisect.bisect_left(nums, i + 1) == i + 1: return i + 1
        return -1
# @lc code=end

