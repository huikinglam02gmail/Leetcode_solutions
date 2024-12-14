#
# @lc app=leetcode id=2596 lang=python3
#
# [2596] Check Knight Tour Configuration
#

# @lc code=start
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        seq = [[-1, -1] for i in range(len(grid) * len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                seq[grid[i][j]] = [i, j]
        if seq[0] != [0, 0]: return False
        for i in range(len(grid) * len(grid) - 1):
            if abs(seq[i][0] - seq[i + 1][0]) * abs(seq[i][1] - seq[i + 1][1]) != 2: return False
        return True
# @lc code=end

