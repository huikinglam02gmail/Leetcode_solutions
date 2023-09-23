#
# @lc app=leetcode id=1914 lang=python3
#
# [1914] Cyclically Rotating a Grid
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= k <= 10^9
    Has to go around the grid clockwise to get grid points of the same ring.
    New coordinates = (i + k) % n
    '''
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        visited = set()
        m, n = len(grid), len(grid[0])
        rings = []
        for i in range(m):
            if i < n and (i, i) not in visited:
                rings.append([])
                j = i
                rings[-1].append([i, j])
                visited.add((i, j))
                while j + 1 < n and (i, j + 1) not in visited:
                    j += 1
                    rings[-1].append([i, j])
                    visited.add((i, j))
                while i + 1 < m and (i + 1, j) not in visited:
                    i += 1
                    rings[-1].append([i, j])
                    visited.add((i, j))
                while j - 1 >= 0 and (i, j - 1) not in visited:
                    j -= 1
                    rings[-1].append([i, j])
                    visited.add((i, j))
                while i - 1 >= 0 and (i - 1, j) not in visited:
                    i -= 1
                    rings[-1].append([i, j])
                    visited.add((i, j))
        
        result = [[0 for j in range(n)] for i in range(m)]
        for i in range(len(rings)):
            for j, [x, y] in enumerate(rings[i]):
                newX, newY = rings[i][(j + k) % len(rings[i])]
                result[x][y] = grid[newX][newY]
        return result
                

# @lc code=end

