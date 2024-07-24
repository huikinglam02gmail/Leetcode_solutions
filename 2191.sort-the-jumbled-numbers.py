#
# @lc app=leetcode id=2191 lang=python3
#
# [2191] Sort the Jumbled Numbers
#

# @lc code=start
from typing import List


class Solution:
    '''
    Each item < 10 ^ 9
    so use string, map, int and sort
    '''
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            numString = str(num)
            newNumString = ""
            for c in numString: newNumString += str(mapping[int(c)])
            result.append([i, int(newNumString)])
        result.sort(key = lambda x: [x[1], x[0]])
        return [nums[i] for i, num in result]
        
# @lc code=end

