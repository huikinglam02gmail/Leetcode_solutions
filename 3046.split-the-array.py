#
# @lc app=leetcode id=3046 lang=python3
#
# [3046] Split the Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    Occurrence of each num cannot exceed 2
    '''
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        occur = {}
        for num in nums: 
            occur[num] = occur.get(num, 0) + 1
            if occur[num] > 2: return False
        return True
# @lc code=end

