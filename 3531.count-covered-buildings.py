#
# @lc app=leetcode id=3531 lang=python3
#
# [3531] Count Covered Buildings
#

# @lc code=start
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x = {}
        y = {}
        for bx, by in buildings:
            if bx not in x: x[bx] = []
            if by not in y: y[by] = []
            x[bx].append(by)
            y[by].append(bx)
        
        for k in x: x[k].sort()
        for k in y: y[k].sort()
        
        result = 0
        for bx, by in buildings:
            if bx != y[by][0] and bx != y[by][-1] and by != x[bx][0] and by != x[bx][-1]: result += 1
        return result

            
# @lc code=end
