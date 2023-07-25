#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    Binary search for the peak    
    '''
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid - 1] < arr[mid] < arr[mid + 1]:
                left = mid
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                right = mid
            elif arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            else:
                return -1
# @lc code=end

