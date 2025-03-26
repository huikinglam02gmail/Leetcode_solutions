#
# @lc app=leetcode id=3219 lang=python3
#
# [3219] Minimum Cost for Cutting Cake II
#

# @lc code=start
from typing import List


class Solution:
    '''
    For each vertical cut, number of horizontal cut increases by 1, and vice versa
    '''
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        hCount = 1
        vCount = 1
        result = 0
        while horizontalCut or verticalCut:
            if horizontalCut and verticalCut:
                if horizontalCut[-1] >= verticalCut[-1]:
                    result += horizontalCut.pop() * vCount
                    hCount += 1
                else:
                    result += verticalCut.pop() * hCount
                    vCount += 1
            else:
                while horizontalCut:
                    result += horizontalCut.pop() * vCount
                    hCount += 1                
                while verticalCut:
                    result += verticalCut.pop() * hCount
                    vCount += 1
        return result

        
# @lc code=end

