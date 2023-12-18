#
# @lc app=leetcode id=2017 lang=python3
#
# [2017] Grid Game
#

# @lc code=start
from typing import List


class Solution:
    '''
    first robot will proceed to next row at some column. If it proceeds at index i, second robot can get max(sum(grid[0][i + 1:]), sum(grid[:i]))
    '''
    def gridGame(self, grid: List[List[int]]) -> int:
        result, top, bottom = float("inf"), sum(grid[0]), 0
        for i in range(len(grid[0])):
            top -= grid[0][i]
            if i > 0: bottom += grid[1][i - 1]
            result = min(result, max(top, bottom))
        return result
# @lc code=end

