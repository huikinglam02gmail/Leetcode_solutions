#
# @lc app=leetcode id=2658 lang=python3
#
# [2658] Maximum Number of Fish in a Grid
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        result = 0
        dq = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    dq.append([i, j])
                    current = grid[i][j]
                    grid[i][j] = 0
                    while dq:
                        x, y = dq.popleft()
                        neigs = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
                        for nx, ny in neigs:
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                                dq.append([nx, ny])
                                current += grid[nx][ny]
                                grid[nx][ny] = 0
                    result = max(result, current)
        return result

# @lc code=end

