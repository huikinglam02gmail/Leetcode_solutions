#
# @lc app=leetcode id=1187 lang=python3
#
# [1187] Make Array Strictly Increasing
#

# @lc code=start
import bisect
from functools import lru_cache
from typing import List


class Solution:
    '''
    This problem is related to dynamic programming
    For example, arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
    We try to work from left to right.
    To get arr1[i:] to be strictly increasing, the necessary and sufficient conditions are:
    1. arr1[i+1:] is strictly increasing
    2. arr1[i+1] > arr1[i]
    We define dp(i, prev) = minimum number of operations (possibly zero) needed to make arr1[i:] strictly increasing, in which prev is the last replaced / looked at element
    We want to know dp(0, -float('inf'))
    at index i with prev, we can choose to swap or not to swap current element with elements in arr2
    However, because we are looking for minimum swaps, we want to swap with a larger element in arr2 than prev, but just larger
    Therefore, binary search would be the way to go in here
    We want to remove duplicates in arr2 and sort it to prepare for that
    For the dp, we have dp(i, prev) = min(1 + dp(i+1, ele), dp(i+1, arr[i]))    
    '''

    @lru_cache(None)
    def dp(self, i, prev):
        if i == len(self.arr1):
            return 0
        result = float('inf')
        # no swap
        if self.arr1[i] > prev:
            result = min(result, self.dp(i+1, self.arr1[i]))
        # swap
        j = bisect.bisect_right(self.arr2, prev)
        if j < len(self.arr2):
            result = min(result, 1 + self.dp(i+1, self.arr2[j]))
        return result
        
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        self.arr2 = sorted(set(arr2))
        self.arr1 = arr1
        result = self.dp(0, -float('inf'))
        if result != float('inf'):
            return result
        else:
            return -1
    # @lc code=end

