#
# @lc app=leetcode id=2784 lang=python3
#
# [2784] Check if Array is Good
#

# @lc code=start
from typing import List


class Solution:
    '''
    We actually know what good array looks like. So just sort and compare
    '''
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        for i in range(n - 1):
            if nums[i] != i + 1: return False
        return nums[n - 1] == n - 1
        
# @lc code=end

