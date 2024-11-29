#
# @lc app=leetcode id=2577 lang=python3
#
# [2577] Minimum Time to Visit a Cell in a Grid

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    There is only 1 case in which we cannot reach (m - 1, n - 1): grid[0][1] > 1 and grid[1][0] > 1
    Otherwise, the shortest time to reach (i, j) would be from one of its neighbor. The cost would be max(t + 1, grid[i][j] + (grid[i][j] - time to reach its neighbour) % 2))
    '''
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        heap = []
        heapq.heappush(heap, [0, 0, 0])
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        visited[0][0] = True
        while heap:
            t, x, y = heapq.heappop(heap)
            if x == m - 1 and y == n - 1: return t
            neigs = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
            for nx, ny in neigs:
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] > t: heapq.heappush(heap, [grid[nx][ny] + 1 - (grid[nx][ny] - t) % 2, nx, ny])
                    else: heapq.heappush(heap, [t + 1, nx, ny])
        return -1
        
# @lc code=end
