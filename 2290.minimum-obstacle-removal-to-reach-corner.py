#
# @lc app=leetcode id=2290 lang=python3
#
# [2290] Minimum Obstacle Removal to Reach Corner
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    Dijkstra algorithm
    edge weight are all 1
    shortest weighted path from 0,0 to m-1, n-1    
    '''
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [float('inf') for _ in range(m*n)]
        dist[0] = grid[0][0]
        heap = [(dist[0], 0, 0)]
        heapq.heapify(heap)
        while heap:
            o, r, c = heapq.heappop(heap)
            if (r, c) == (m-1, n-1):
                return o
            else:
                for i, j in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
                    if i >= 0 and j >= 0 and i < m and j < n:
                        new_dist = grid[i][j] + o
                        if grid[i][j] + o < dist[n*i+j]:
                            dist[n*i+j] = new_dist
                            heapq.heappush(heap, (new_dist, i, j))
        return dist[n*(m-1)+n-1]
# @lc code=end

