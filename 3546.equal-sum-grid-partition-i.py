#
# @lc app=leetcode id=3546 lang=python3
#
# [3546] Equal Sum Grid Partition I
#

from typing import List

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = [0]
        for i in range(len(grid)): rows.append(rows[-1] + sum(grid[i]))
        cols = [0]
        for j in range(len(grid[0])):
            cols.append(cols[-1])
            for i in range(len(grid)): cols[-1] += grid[i][j]
        for i in range(1, len(rows)):
            if rows[i] == rows[-1] - rows[i]: return True
        for j in range(1, len(cols)):
            if cols[j] == cols[-1] - cols[j]: return True
        return False
# @lc code=end

