#
# @lc app=leetcode id=2087 lang=python3
#
# [2087] Minimum Cost Homecoming of a Robot in a Grid
#

# @lc code=start
from typing import List


class Solution:
    '''
    There's no point going up one row and later go back down. 
    '''
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        result = 0
        sign = 1 if startPos[0] <= homePos[0] else -1
        for i in range(startPos[0] + sign, homePos[0] + sign, sign): result += rowCosts[i]
        sign = 1 if startPos[1] <= homePos[1] else -1
        for i in range(startPos[1] + sign, homePos[1] + sign, sign): result += colCosts[i]
        return result
        
# @lc code=end

