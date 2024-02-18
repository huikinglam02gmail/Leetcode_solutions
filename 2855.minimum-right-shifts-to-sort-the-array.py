#
# @lc app=leetcode id=2855 lang=python3
#
# [2855] Minimum Right Shifts to Sort the Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    First find where the max and min are at.
    Suppose they are at i and j, then (i + 1) % n == j
    The rest is to check if nums are strictly increasing from j to i. If so, the answer is n - 1 - i
    '''
    def minimumRightShifts(self, nums: List[int]) -> int:
        maxSoFar, minSoFar, i, j, n = 0, 101, -1, -1, len(nums)
        for k in range(n):
            if nums[k] > maxSoFar: maxSoFar, i = nums[k], k
            if nums[k] < minSoFar: minSoFar, j = nums[k], k
        if (i + 1) % n != j: return -1
        l = j
        while l != i and nums[(l + 1) % n] > nums[l]:
            l += 1
            l %= n
        if l == i: return n - 1 - i
        else: return -1

# @lc code=end

