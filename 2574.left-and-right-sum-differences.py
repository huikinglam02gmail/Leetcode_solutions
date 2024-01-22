#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#

# @lc code=start
from typing import List


class Solution:
    '''
    prefix Sum
    '''
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        result = []
        for i, num in enumerate(nums):
            result.append(abs(prefixSum[-1] - prefixSum[i + 1] - prefixSum[i]))
        return result
        
# @lc code=end

