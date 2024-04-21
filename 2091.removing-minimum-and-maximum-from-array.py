#
# @lc app=leetcode id=2091 lang=python3
#
# [2091] Removing Minimum and Maximum From Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    Identify indices of max and min
    There are 3 possibilities:
    1. delete both from left
    2. delete min(minInd, maxInd) from left and max(minInd, maxInd) from right
    3. delete both from right
    '''
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        result = [0] * 3
        maxInd, maxNum, minInd, minNum = -1, -100001, -1, 100001
        for i, num in enumerate(nums):
            if num > maxNum:
                maxNum = num
                maxInd = i
            if num < minNum:
                minNum = num
                minInd = i
        result[0] = max(maxInd, minInd) + 1
        result[2] = n - min(maxInd, minInd)
        result[1] = min(minInd, maxInd) + 1 + n - max(minInd, maxInd)
        return min(result)
        
# @lc code=end

