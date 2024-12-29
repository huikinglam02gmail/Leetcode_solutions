#
# @lc app=leetcode id=3402 lang=python3
#
# [3402] Minimum Operations to Make Columns Strictly Increasing
#

# @lc code=start
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        result = 0
        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                result += max(0, grid[i - 1][j] + 1 - grid[i][j])
                grid[i][j] = max(grid[i][j], grid[i - 1][j] + 1)
        return result
# @lc code=end

