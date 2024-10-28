#
# @lc app=leetcode id=3232 lang=python3
#
# [3232] Find if Digit Game Can Be Won
#

# @lc code=start
from typing import List


class Solution:
    '''
    sort + prefix sum
    '''
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(num for num in nums if num < 10) != sum(num for num in nums if num >= 10)
# @lc code=end

