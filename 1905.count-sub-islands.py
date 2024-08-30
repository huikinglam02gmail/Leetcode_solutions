#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    We can BFS the islands for both grid1 and grid2
    For each island in grid1. we modify the grid to change 1 to island count
    Then when we BFS for islands in grid2, we ask if all grids has the same value in grid1    
    '''
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n, island_counter = len(grid1), len(grid1[0]), 2
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1:
                    dq = deque()
                    dq.append((i,j))
                    grid1[i][j] = island_counter
                    while dq:
                        x, y = dq.popleft()
                        neigs = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                        for neig in neigs:
                            xn, yn = neig
                            if xn >= 0 and yn >= 0 and xn < m and yn < n and grid1[xn][yn] == 1:
                                grid1[xn][yn] = island_counter
                                dq.append(neig)
                    island_counter += 1
        
        result = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    dq = deque()
                    dq.append((i,j))
                    grid2[i][j] = 0
                    parent, same_parent = grid1[i][j], True
                    while dq:
                        x, y = dq.popleft()
                        neigs = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                        for neig in neigs:
                            xn, yn = neig
                            if xn >= 0 and yn >= 0 and xn < m and yn < n and grid2[xn][yn] == 1:
                                dq.append(neig)
                                grid2[xn][yn] = 0
                                same_parent= same_parent and  grid1[xn][yn] == parent
                    if same_parent and parent > 1: result += 1
        return result
# @lc code=end

