#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    arr is already sorted. So we can separate arr into 4 parts, and binary search for the answer
    '''
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n // 4 == 0: return arr[0]
        for i in range(0, n, n // 4):
            if bisect.bisect_right(arr, arr[i]) - bisect.bisect_left(arr, arr[i]) > n // 4:
                return arr[i]
        return -1
# @lc code=end

