#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#

# @lc code=start
from typing import List


class Solution:
    '''
    We can explore all the possibilities by backtracking
    There is a testcase of no 0s at all in the grid. Using the backtracking algorithm would give TLE, so I included the check zero part    
    '''    
    def dfs(self, x, y):
        if x < 0 or y < 0 or x >= len(self.grid) or y >= len(self.grid[0]) or self.grid[x][y] == 0: return 0
        original = self.grid[x][y]
        result = 0
        neigs = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        self.grid[x][y] = 0
        for xn, yn in neigs: result = max(result, self.dfs(xn, yn))
        self.grid[x][y] = original
        return result + original
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n, total = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
        
        self.grid = grid
        m, n, result = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                result = max(result, self.dfs(i,j))
                if result == total: return total
        return result
# @lc code=end

