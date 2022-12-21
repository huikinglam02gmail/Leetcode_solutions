#
# @lc app=leetcode id=1559 lang=python3
#
# [1559] Detect Cycles in 2D Grid
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    # pretty obvious we can conduct BFS from each unvisited node
    # To detect cycles, we can mark a node's parent, such that it will avoid backtracking and still recognize cycles
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    dq = deque()
                    character = grid[i][j]
                    dq.append([i, j, -1, -1])
                    visited.add((i,j))
                    while dq:
                        currX, currY, lastX, lastY = dq.popleft()
                        neigs = [[currX + 1, currY], [currX - 1, currY], [currX, currY + 1], [currX, currY - 1]]
                        for nxtX, nxtY in neigs:
                            if m > nxtX >= 0 <= nxtY < n and (nxtX != lastX or nxtY != lastY) and grid[nxtX][nxtY] == character:
                                if (nxtX, nxtY) not in visited:
                                    dq.append([nxtX, nxtY, currX, currY])
                                    visited.add((nxtX, nxtY))
                                else:
                                    return True       
        return False
                        

        
# @lc code=end

