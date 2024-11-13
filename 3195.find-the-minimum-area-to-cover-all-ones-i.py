#
# @lc app=leetcode id=3195 lang=python3
#
# [3195] Find the Minimum Area to Cover All Ones I
#

# @lc code=start
from typing import List


class Solution:
    '''
    Get all x and y coordinates of 1s, return (maxx - minx + 1) * (maxy - miny + 1)
    '''
    def minimumArea(self, grid: List[List[int]]) -> int:
        maxX, maxY, minX, minY = -float("inf"), -float("inf"), float("inf"), float("inf")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxX = max(maxX, i)
                    minX = min(minX, i)
                    maxY = max(maxY, j)
                    minY = min(minY, j)
        return (maxX - minX + 1) * (maxY - minY + 1)
# @lc code=end

