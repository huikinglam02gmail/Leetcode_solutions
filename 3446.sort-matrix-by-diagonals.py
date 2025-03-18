#
# @lc app=leetcode id=3446 lang=python3
#
# [3446] Sort Matrix by Diagonals
#

# @lc code=start
from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        TopRight = []
        BottomLeft = []
        n = len(grid)
        for j in range(n - 1, 0, -1): TopRight.append([0, j])
        for i in range(n): BottomLeft.append([i, 0])
        for j in range(len(TopRight)):
            currentCoords = []
            vals = []
            x, y = TopRight[j]
            while x < n and y < n:
                currentCoords.append([x, y])
                vals.append(grid[x][y])
                x += 1
                y += 1
            vals.sort()
            for i in range(len(currentCoords)): grid[currentCoords[i][0]][currentCoords[i][1]] = vals[i]
        for j in range(len(BottomLeft)):
            currentCoords = []
            vals = []
            x, y = BottomLeft[j]
            while x < n and y < n:
                currentCoords.append([x, y])
                vals.append(grid[x][y])
                x += 1
                y += 1
            vals.sort(reverse=True)
            for i in range(len(currentCoords)): grid[currentCoords[i][0]][currentCoords[i][1]] = vals[i]
        return grid
            
# @lc code=end

