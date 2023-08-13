#
# @lc app=leetcode id=2369 lang=python3
#
# [2369] Check if There is a Valid Partition For The Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    dp[i][j] = nums[:i + 1] has a valid partition which the last valid subarray obeys condition j
    '''
    def validPartition(self, nums: List[int]) -> bool:
        b, c, d = False, True, True
        n = len(nums)
        for i in range(1, n, 1):
            a = False
            if nums[i] == nums[i - 1]:
                a |= c
            if i > 1 and nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                a |= d
            if i > 1 and nums[i] == nums[i - 1] + 1 and nums[i] == nums[i - 2] + 2:
                a |= d
            b, c, d = a, b, c
        return a
# @lc code=end

