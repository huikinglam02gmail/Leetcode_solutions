#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    First find where is the shift point Then find num
    The algorithm to find the minimum is given in Leetcode 153  
    '''
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l < r - 1:
            mid = l + (r - l) // 2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return (l + 1) % len(nums)
                
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        elif nums[-1] == target:
            return len(nums) - 1
        else:
            ind = self.findMin(nums)
            if nums[0] < target:
                result = bisect.bisect_left(nums[:ind], target)
                return result if nums[result] == target else -1
            else:
                result = bisect.bisect_left(nums[ind:], target)
                return -1 if result + ind == len(nums) or nums[result + ind] != target else ind + result
# @lc code=end

