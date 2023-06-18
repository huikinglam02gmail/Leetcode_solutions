#
# @lc app=leetcode id=2328 lang=python3
#
# [2328] Number of Increasing Paths in a Grid
#

# @lc code=start

from functools import lru_cache
from typing import List


class Solution:
    '''
    DP problem
    bottom-up DP seems really tricky because the paths might not be going in only one direction. The edges are base case in one direction but not so in other directions.
    Therefore I use DFS + memo approach for this problem
    Just record the number of strictly increasing path starting from (i,j)    
    '''

    @lru_cache(None)
    def dfs(self, row, col):
        result = 1
        if row + 1 < len(self.grid) and self.grid[row+1][col] > self.grid[row][col]: 
            result += self.dfs(row+1, col)
            result %= self.MOD
        if col + 1 < len(self.grid[0])  and self.grid[row][col+1] > self.grid[row][col]: 
            result += self.dfs(row, col+1)
            result %= self.MOD
        if row > 0  and self.grid[row-1][col] > self.grid[row][col]: 
            result += self.dfs(row-1, col)
            result %= self.MOD
        if col > 0  and self.grid[row][col-1] > self.grid[row][col]: 
            result += self.dfs(row, col-1)
            result %= self.MOD
        return result
        
    def countPaths(self, grid: List[List[int]]) -> int:
        self.grid = grid
        result = 0
        self.MOD = pow(10,9) + 7
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                result += self.dfs(i, j)
                result %= self.MOD
        return result
# @lc code=end

