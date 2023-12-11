#
# @lc app=leetcode id=2012 lang=python3
#
# [2012] Sum of Beauty in the Array
#

# @lc code=start
from typing import List

from sortedcontainers import SortedList


class Solution:
    '''
    Use two sortedList left and right to denote left and right of each index
    Then iterate from i = 1 to n - 2
    '''
    def sumOfBeauties(self, nums: List[int]) -> int:
        left, right = SortedList(), SortedList()
        n, result = len(nums), 0
        for i in range(n):
            right.add([nums[i], i])
        for i in range(n):
            right.remove([nums[i], i])
            if 0 < i < n - 1: 
                if nums[i - 1] < nums[i] < nums[i + 1]: result += 1
                if left[-1][0] < nums[i] < right[0][0]: result += 1
            left.add([nums[i], i])
        return result

        
# @lc code=end

