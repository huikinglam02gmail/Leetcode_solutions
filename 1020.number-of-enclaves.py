#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
from collections import deque
from typing import Deque, List


class Solution:
    '''
    BFS from edge 1s and label its connected components 0.
    Then count how many inside is still 1
    '''
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n, result = len(grid), len(grid[0]), 0

        def bfs(x, y):
            if grid[x][y] == 1:
                dq = deque()
                dq.append([x, y])
                grid[x][y] = 0
                while dq:
                    x, y = dq.popleft()
                    neigs = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
                    for x_n, y_n in neigs:
                        if x_n >= 0 and x_n < m and y_n >= 0 and y_n < n and grid[x_n][y_n] == 1:
                            dq.append([x_n, y_n])
                            grid[x_n][y_n] = 0

        for i in range(m):
            bfs(i, 0)
            bfs(i, n - 1)
        
        for j in range(n):
            bfs(0, j)
            bfs(m - 1, j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += 1
        
        return result
            
# @lc code=end

