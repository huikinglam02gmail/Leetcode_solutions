#
# @lc app=leetcode id=3071 lang=python3
#
# [3071] Minimum Operations to Write the Letter Y on a Grid
#

# @lc code=start
from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        onY = [0] * 3
        offY = [0] * 3
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i <= n // 2 and i == j: onY[grid[i][j]] += 1
                elif i <= n // 2 and j == n - 1 - i: onY[grid[i][j]] += 1
                elif i > n // 2 and j  == n // 2: onY[grid[i][j]] += 1
                else: offY[grid[i][j]] += 1
        return min(onY[1] + onY[2] + offY[0] + min(offY[1], offY[2]), onY[0] + onY[2] + offY[1] + min(offY[0], offY[2]), onY[0] + onY[1] + offY[2] + min(offY[0], offY[1]))
        
        
# @lc code=end

