#
# @lc app=leetcode id=2679 lang=python3
#
# [2679] Sum in a Matrix
#

# @lc code=start
from typing import List


class Solution:
    '''
    Sort each row
    '''
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums: row.sort(reverse=True)
        result = 0
        for i in range(len(nums[0])):
            current = 0
            for j in range(len(nums)): current =  max(current, nums[j][i])
            result += current
        return result
        
# @lc code=end

