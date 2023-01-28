#
# @lc app=leetcode id=1630 lang=python3
#
# [1630] Arithmetic Subarrays
#

# @lc code=start
from typing import List


class Solution:
    # No shortcut, just brute force

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff, n = arr[1] - arr[0], len(arr)
        for i in range(1,n-1):
            if arr[i] + diff != arr[i+1]:
                return False
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for li, ri in zip(l, r):
            result.append(self.canMakeArithmeticProgression(nums[li:ri+1]))
        return result
# @lc code=end

