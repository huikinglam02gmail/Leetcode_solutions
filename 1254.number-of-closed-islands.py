#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    BFS from the border to convert all connected land (0) to sea (1). Then number of islands    
    '''
    
    def boundary_islands_removal(self, x, y):
        if self.grid[x][y] == 0:
            dq = deque()
            dq.append([x, y])
            self.grid[x][y] = 1
            while dq:
                x, y = dq.popleft()
                neigs = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
                for x_n, y_n in neigs:
                    if x_n >= 0 and x_n < self.m and y_n >= 0 and y_n < self.n and self.grid[x_n][y_n] == 0:
                        dq.append([x_n, y_n])
                        self.grid[x_n][y_n] = 1
        
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        for i in range(self.m):
            self.boundary_islands_removal(i, 0)
            self.boundary_islands_removal(i, self.n-1)
        for i in range(self.n):
            self.boundary_islands_removal(0, i)
            self.boundary_islands_removal(self.m-1, i)
        
        result = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    result += 1
                    self.boundary_islands_removal(i, j)
        return result
# @lc code=end

