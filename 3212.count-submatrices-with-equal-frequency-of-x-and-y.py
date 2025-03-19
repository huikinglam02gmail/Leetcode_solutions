#
# @lc app=leetcode id=3212 lang=python3
#
# [3212] Count Submatrices With Equal Frequency of X and Y
#

# @lc code=start
from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        lastRow = [[0, 0] for j in range(n)]
        for i in range(m):
            thisRow = []
            countX, countY = 0, 0
            for j in range(n):
                if grid[i][j] == 'X': countX += 1
                if grid[i][j] == 'Y': countY += 1
                thisRow.append([countX, countY])
            for j in range(n):
                thisRow[j][0] += lastRow[j][0]
                thisRow[j][1] += lastRow[j][1]
                if thisRow[j][0] > 0 and thisRow[j][1] == thisRow[j][0]: result += 1
            lastRow = thisRow.copy()
        return result


# @lc code=end

