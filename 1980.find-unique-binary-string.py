#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
from typing import List


class Solution:
    '''
    n == nums.length
    1 <= n <= 16
    nums[i].length == n
    so it's super easy. Just try from 0 upwards and report the first one missing
    '''
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        i = 0
        while i < (1 << n):
            if bin(i)[2:].zfill(n) not in nums:
                return bin(i)[2:].zfill(n)
            else:
                i += 1
        return ""
# @lc code=end

