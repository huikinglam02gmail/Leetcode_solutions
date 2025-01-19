#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def inside(self, row, col, m, n):
        if row < 0:
            return False
        elif col < 0:
            return False
        elif row >= m:
            return False
        elif col >= n:
            return False
        return True
                
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []
        visited = set()
        result = 0
        m, n = len(heightMap), len(heightMap[0])
        # Add the boundary
        for i in range(m):
            heapq.heappush(heap, [heightMap[i][0], i, 0])
            visited.add((i, 0))
            heapq.heappush(heap, [heightMap[i][n - 1], i, n - 1])
            visited.add((i, n - 1))
        # Add the boundary
        for i in range(n):
            if (0, i) not in visited:
                heapq.heappush(heap, [heightMap[0][i], 0, i])
                visited.add((0, i))
            if (m - 1, i) not in visited:
                heapq.heappush(heap, [heightMap[m - 1][i], m - 1, i])
                visited.add((m-1, i))
        neighbours = [[-1, 0],[1, 0],[0, -1],[0, 1]]
        
        while heap:
            h, x, y = heapq.heappop(heap)
            for j in range(len(neighbours)):
                if self.inside(x + neighbours[j][0], y + neighbours[j][1], m, n) and (x + neighbours[j][0], y + neighbours[j][1]) not in visited:
                    result += max(0, h - heightMap[x + neighbours[j][0]][y + neighbours[j][1]])
                    heapq.heappush(heap, [max(heightMap[x + neighbours[j][0]][y + neighbours[j][1]], h), x + neighbours[j][0], y + neighbours[j][1]])
                    visited.add((x + neighbours[j][0], y + neighbours[j][1]))
        return result
# @lc code=end

