#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        elif n == 2: return nums.index(max(nums))
        else:
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == n -1 or nums[mid + 1] < nums[mid]):
                    return mid
                elif nums[mid - 1] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
# @lc code=end

