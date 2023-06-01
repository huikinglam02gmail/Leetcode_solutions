#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Shortest path: BFS would be good   
    '''

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        dq, visited, steps = deque(), set(), 1
        dq.append((0,0))
        visited.add((0,0))
        while dq:
            for i in range(len(dq)):
                x, y = dq.popleft()
                if x == m-1 and y == n-1:
                    return steps
                neighbours = [(x-1, y-1), (x-1, y), (x-1,y+1), (x, y+1), (x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1)]
                for nx, ny in neighbours:
                    if nx >= 0 and nx < m and ny >= 0 and ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                        dq.append((nx,ny))
                        visited.add((nx, ny))
            steps += 1
        return -1
# @lc code=end

