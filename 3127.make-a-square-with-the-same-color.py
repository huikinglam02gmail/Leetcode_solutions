#
# @lc app=leetcode id=3127 lang=python3
#
# [3127] Make a Square with the Same Color
#

# @lc code=start
from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m - 1):
            for j in range(n - 1):
                current = 0
                if grid[i][j] == "B": current += 1
                if grid[i + 1][j] == "B": current += 1
                if grid[i][j + 1] == "B": current += 1
                if grid[i + 1][j + 1] == "B": current += 1
                if current != 2: return True
        return False
# @lc code=end

