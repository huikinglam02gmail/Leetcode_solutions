#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        width = len(grid)
        height = len(grid[0])
        touching = 0
        count = 0
        for i in range(width):
            for j in range(height):
                if grid[i][j] == 1:
                    count += 1
                if i != width- 1 and grid[i][j] == 1 and grid[i + 1][j] == 1:
                    touching += 1
                if j != height - 1 and grid[i][j] == 1 and grid[i][j + 1] == 1:
                    touching += 1
        return count * 4 - 2 * touching        
# @lc code=end

