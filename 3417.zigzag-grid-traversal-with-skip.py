#
# @lc app=leetcode id=3417 lang=python3
#
# [3417] Zigzag Grid Traversal With Skip
#

# @lc code=start
from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        x, y, dir = 0, 0, 1
        result = []
        while x < len(grid):
            if 0 <= y < len(grid[0]): result.append(grid[x][y])
            y += 2 * dir
            if y >= len(grid[0]) or y < 0:
                x += 1
                dir = -dir
                y += dir
        return result

# @lc code=end

