#
# @lc app=leetcode id=3619 lang=python3
#
# [3619] Count Islands With Total Value Divisible by K
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n, result = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    current = 0
                    dq = deque([(i, j)])
                    current += grid[i][j]
                    grid[i][j] = 0
                    while dq:
                        x, y = dq.popleft()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                                current += grid[nx][ny]
                                grid[nx][ny] = 0
                                dq.append((nx, ny))
                    if current % k == 0: result += 1
        return result
                    
# @lc code=end

