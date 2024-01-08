#
# @lc app=leetcode id=2239 lang=python3
#
# [2239] Find Closest Number to Zero
#

# @lc code=start
from typing import List


class Solution:
    '''
    sort by [abs(num), - num]
    '''
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: [abs(x), - x])
        return nums[0]
# @lc code=end

