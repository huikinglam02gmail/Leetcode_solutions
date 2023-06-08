#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
from typing import List


class Solution:
    '''
    walk a pointer from top right corner to bottom    
    '''
    def countNegatives(self, grid: List[List[int]]) -> int:
        result, m, n = 0, len(grid), len(grid[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if grid[x][y] >= 0:
                result += n - 1 - y
                x += 1
            else:
                y -= 1
        if y < 0:
            result += (m - x)*n
        return result
# @lc code=end

